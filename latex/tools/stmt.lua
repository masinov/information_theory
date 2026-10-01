-- Pandoc filter: structure (parts, sections), numbered statements, proofs.
local kinds = {
  Theorem = 'thmplain', Proposition = 'thmplain', Lemma = 'thmplain', Corollary = 'thmplain', Fact = 'thmplain',
  Conjecture = 'thmplain', Definition = 'thmdef', Assumption = 'thmdef',
  Remark = 'thmrem', Example = 'thmrem', Problem = 'thmrem',
}

local function tex(inlines)
  local s = pandoc.write(pandoc.Pandoc({ pandoc.Plain(inlines) }), 'latex')
  return (s:gsub('%s+$', ''))
end

local function raw(s) return pandoc.RawBlock('latex', s) end

local function strip_leading(inlines, pred)
  -- drop first element if pred, then one following space
  if inlines[1] and pred(inlines[1]) then
    inlines:remove(1)
    if inlines[1] and (inlines[1].t == 'Space' or inlines[1].t == 'SoftBreak') then inlines:remove(1) end
    return true
  end
  return false
end

function Header(h)
  local plain = pandoc.utils.stringify(h.content)
  if h.level == 2 then
    local pt = plain:match('^Part%s+[IVXL]+:%s*(.*)$')
    if pt then
      local inl = pandoc.List(h.content)
      inl:remove(1); if inl[1] and inl[1].t == 'Space' then inl:remove(1) end
      inl:remove(1); if inl[1] and inl[1].t == 'Space' then inl:remove(1) end
      return raw('\\part{' .. tex(inl) .. '}')
    end
    local ap = plain:match('^Appendix%s+%u:%s*(.*)$')
    if ap then
      local inl = pandoc.List(h.content)
      for _ = 1, 2 do inl:remove(1); if inl[1] and inl[1].t == 'Space' then inl:remove(1) end end
      return raw('\\appsection{' .. tex(inl) .. '}')
    end
  end
  local pre, num = plain:match('^(%u?%.?)(%d+[%d%.]*)%.?%s')
  local letter = plain:match('^(%u)%.%d')
  if h.level >= 2 and num and (h.level == 2 or h.level == 3) then
    local inl = pandoc.List(h.content)
    inl:remove(1); if inl[1] and (inl[1].t == 'Space') then inl:remove(1) end
    local n1, n2 = num:match('^(%d+)%.?(%d*)')
    local label = (letter and (letter .. '.') or '') .. num:gsub('%.$', '')
    if h.level == 2 then
      return raw(string.format('\\secn{%d}{%s}{%s}', tonumber(n1), label, tex(inl)))
    else
      return raw(string.format('\\subsecn{%d}{%s}{%s}', tonumber(n2 ~= '' and n2 or n1), label, tex(inl)))
    end
  end
  if h.level == 4 then return pandoc.Header(3, h.content) end
  return nil
end

function HorizontalRule() return {} end

local function is_proof(b)
  if b.t ~= 'Para' or not b.content[1] or b.content[1].t ~= 'Emph' then return false end
  return pandoc.utils.stringify(b.content[1]):match('^Proof') ~= nil
end

local function drop_square(blocks)
  local last = blocks[#blocks]
  if last and (last.t == 'Para' or last.t == 'Plain') then
    local c = last.content
    local n = #c
    while n > 0 and (c[n].t == 'Space' or c[n].t == 'SoftBreak') do n = n - 1 end
    if n > 0 and c[n].t == 'Math' and c[n].text:match('^%s*\\square%s*$') then
      for _ = #c, n, -1 do c:remove(n) end
    end
  end
end

function BlockQuote(bq)
  local blocks = pandoc.List(bq.content)
  local first = blocks[1]
  if not (first and first.t == 'Para' and first.content[1] and first.content[1].t == 'Strong') then
    return nil
  end
  local head = tex(first.content[1].content)
  local kind, rest
  local we = head:match('^Worked example%s+(%u)')
  local env, label, display
  if we then
    kind = 'Worked example'; env = 'thmrem'
    rest = head:gsub('^Worked example%s+%u', '')
    label = 'ex' .. we; display = 'Worked example ' .. we
  else
    kind = head:match('^(%a+)')
    env = kinds[kind or '']
    if not env then return nil end
    rest = head:sub(#kind + 1)
    local num = rest:match('^%s+([%u]?%.?[%d%.]*%d)')
    if not num then return nil end
    local prime = rest:match('^%s+[%u]?%.?[%d%.]*%d(′)') and '′' or ''
    label = num .. prime
    display = kind .. ' ' .. label
    rest = rest:gsub('^%s+[%u]?%.?[%d%.]*%d', '')
    if prime ~= '' then rest = rest:sub(#prime + 1) end
  end
  local name = rest:match('^%s*%((.*)%)%.?%s*$')
  local note = display:gsub(' ', '~')
  note = '\\hypertarget{stmt:' .. label .. '}{' .. note .. '}'
  if name then note = note .. '\\ {\\normalfont\\upshape(' .. name .. ')}' end
  -- remaining inlines of first para
  local inl = pandoc.List(first.content)
  inl:remove(1)
  if inl[1] and (inl[1].t == 'Space' or inl[1].t == 'SoftBreak') then inl:remove(1) end
  local out = pandoc.List()
  out:insert(raw('\\begin{' .. env .. '}[' .. note .. ']'))
  if #inl > 0 then out:insert(pandoc.Para(inl))
  elseif blocks[2] and (blocks[2].t == 'OrderedList' or blocks[2].t == 'BulletList') then
    out:insert(raw('\\par\\nopagebreak'))
  end
  local i = 2
  local proof_at
  while i <= #blocks do
    if is_proof(blocks[i]) then proof_at = i; break end
    out:insert(blocks[i]); i = i + 1
  end
  out:insert(raw('\\end{' .. env .. '}'))
  if proof_at then
    local pr = blocks[proof_at]
    local pname = pandoc.utils.stringify(pr.content[1]):gsub('%.%s*$', '')
    local pin = pandoc.List(pr.content)
    pin:remove(1)
    if pin[1] and (pin[1].t == 'Space' or pin[1].t == 'SoftBreak') then pin:remove(1) end
    local pb = pandoc.List({ pandoc.Para(pin) })
    for j = proof_at + 1, #blocks do pb:insert(blocks[j]) end
    drop_square(pb)
    out:insert(raw(pname == 'Proof' and '\\begin{proof}' or ('\\begin{proof}[' .. pname .. '.]')))
    for _, b in ipairs(pb) do if not (b.t == 'Para' and #b.content == 0) then out:insert(b) end end
    out:insert(raw('\\end{proof}'))
  end
  return out
end

-- Table column widths proportional to content length (pandoc otherwise splits evenly when cells are long).
function Table(tbl)
  local ncol = #tbl.colspecs
  local tot = {}
  local rows = 0
  for i = 1, ncol do tot[i] = 0 end
  local function scan(row)
    for i, cell in ipairs(row.cells) do
      if i <= ncol then
        local len = #pandoc.utils.stringify(cell.contents)
        tot[i] = tot[i] + math.min(len, 90)
      end
    end
  end
  for _, r in ipairs(tbl.head.rows) do scan(r); rows = rows + 1 end
  for _, b in ipairs(tbl.bodies) do for _, r in ipairs(b.body) do scan(r); rows = rows + 1 end end
  if rows == 0 then return nil end
  local w, sum = {}, 0
  for i = 1, ncol do w[i] = math.max(20, tot[i] / rows); sum = sum + w[i] end
  for i = 1, ncol do tbl.colspecs[i] = { tbl.colspecs[i][1], w[i] / sum } end
  return tbl
end
