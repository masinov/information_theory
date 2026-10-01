-- Over-wide display equations: stack at top-level \qquad, or break a long relation chain.
local function est_width(m)
  m = m:gsub('\\text%{([^}]*)%}', '%1'):gsub('\\mathrm%{([^}]*)%}', '%1')
  m = m:gsub('\\%a+', function(c) if c == '\\quad' or c == '\\qquad' then return '' end return 'X' end)
  m = m:gsub('\\[;:,! ]', ''):gsub('[{}\\_%^&%s]', '')
  return #m
end

-- start/end positions of top-level occurrences of the literal token `tok`
local function top_level(m, tok)
  local res, depth, i, n = {}, 0, 1, #m
  while i <= n do
    local c = m:sub(i, i)
    if c == '{' or c == '(' or c == '[' then depth = depth + 1
    elseif c == '}' or c == ')' or c == ']' then depth = math.max(0, depth - 1)
    elseif depth == 0 and m:sub(i, i + #tok - 1) == tok then
      local after = m:sub(i + #tok, i + #tok)
      if not (tok:sub(1, 1) == '\\' and after:match('%a')) then
        table.insert(res, { i, i + #tok - 1 })
      end
    end
    i = i + 1
  end
  return res
end

local function trim(s) return (s:gsub('^%s+', ''):gsub('%s+$', '')) end

local function split_display(m)
  local w = est_width(m)
  local qs = top_level(m, '\\qquad')
  if w >= 50 and #qs > 0 then
    local rows, last = {}, 1
    for _, p in ipairs(qs) do table.insert(rows, trim(m:sub(last, p[1] - 1))); last = p[2] + 1 end
    table.insert(rows, trim(m:sub(last)))
    return '\\begin{gathered}' .. table.concat(rows, ' \\\\ ') .. '\\end{gathered}'
  end
  if w >= 72 then
    local best, bestd = nil, math.huge
    for _, tok in ipairs({ '=', '\\le', '\\approx' }) do
      for _, p in ipairs(top_level(m, tok)) do
        local mid = p[1] / #m
        local d = math.abs(mid - 0.5)
        if mid > 0.3 and mid < 0.75 and d < bestd then best, bestd = p, d end
      end
    end
    if best then
      local a, b = m:sub(1, best[1] - 1), m:sub(best[1])
      a = trim((a:gsub('\\;%s*$', '')))
      b = trim(b)
      return '\\begin{gathered}' .. a .. ' \\\\ {}\\qquad ' .. b .. '\\end{gathered}'
    end
  end
  return nil
end

function Math(el)
  if el.mathtype == 'DisplayMath' then
    local r = split_display(el.text)
    if r then return pandoc.Math('DisplayMath', r) end
  end
  return nil
end
