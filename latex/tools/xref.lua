-- Pandoc filter (runs after stmt.lua): hyperlink textual cross-references.
local here = debug.getinfo(1, 'S').source:sub(2):match('^(.*)[/\\]tools[/\\]') or '.'
local L = dofile(here .. '/build/labels.lua')

local kind_words = {
  Definition = true, Definitions = true, Theorem = true, Theorems = true, Proposition = true, Propositions = true,
  Lemma = true, Lemmas = true, Corollary = true, Corollaries = true, Fact = true, Remark = true, Remarks = true,
  Conjecture = true, Assumption = true, Example = true, Def = true, ['Def.'] = true, Prop = true, ['Prop.'] = true,
  Thm = true, ['Thm.'] = true, Cor = true, ['Cor.'] = true, Lem = true, ['Lem.'] = true,
}

local function split_trailing(s)
  -- "6.5(3)," -> core "6.5", tail "(3),"
  local core = s:match('^([%u]?%.?%d[%d%.]*%d%l?)') or s:match('^([%u]?%.?%d%l?)')
  if not core then return nil end
  local tail = s:sub(#core + 1)
  if tail:sub(1, #'′') == '′' then core = core .. '′'; tail = tail:sub(#'′' + 1) end
  return core, tail
end

function Inlines(inlines)
  local out = pandoc.List()
  local i, changed = 1, false
  while i <= #inlines do
    local el = inlines[i]
    local nxt, nxt2 = inlines[i + 1], inlines[i + 2]
    if el.t == 'Str' and kind_words[el.text] and nxt and (nxt.t == 'Space' or nxt.t == 'SoftBreak') and nxt2 and nxt2.t == 'Str' then
      local core, tail = split_trailing(nxt2.text)
      if core and L.stmts[core] then
        out:insert(pandoc.RawInline('latex', '\\hyperlink{stmt:' .. core .. '}{' .. el.text .. '~' .. core .. '}'))
        if tail ~= '' then out:insert(pandoc.Str(tail)) end
        i = i + 3; changed = true
        goto continue
      end
    end
    if el.t == 'Str' and el.text:match('^§') then
      local core, tail = split_trailing(el.text:sub(#'§' + 1))
      if core and L.secs[core] then
        out:insert(pandoc.RawInline('latex', '\\hyperlink{sec:' .. core .. '}{§' .. core .. '}'))
        if tail ~= '' then out:insert(pandoc.Str(tail)) end
        i = i + 1; changed = true
        goto continue
      end
    end
    out:insert(el); i = i + 1
    ::continue::
  end
  if changed then return out end
  return nil
end
