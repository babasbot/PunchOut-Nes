function done()
  return won() or lost()
end

function reward()
  return time() / (knock_downs() + 1) + (1/100000 * score() * time()^2 + 1)
end

function score()
  return data.score_100000 * 100000 +
         data.score_010000 * 10000  +
         data.score_001000 * 1000   +
         data.score_000100 * 100    +
         data.score_000010 * 10     +
         data.score_000001
end

function knock_downs()
  return data.knock_downs
end

function time()
  return data.clock_minutes    * 60 +
         data.clock_seconds_x0 * 10 +
         data.clock_seconds_0x
end

function won()
  return decision_win() or tko_win() or ko_win()
end

function decision_win()
  return data.fight_status == 250
end

function tko_win()
  return data.fight_status == 252
end

function ko_win()
  return data.fight_status == 254
end

function lost()
  return decision_lost() or tko_lost() or ko_lost()
end

function decision_lost()
  return data.fight_status == 249
end

function tko_lost()
  return data.fight_status == 251
end

function ko_lost()
  return data.fight_status == 253
end
