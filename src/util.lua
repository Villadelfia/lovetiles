-- returns a list of quads given:
-- tilesw: amount of horizontal tiles
-- tilesh: amount of vertical tiles
-- tilew: horizontal size of a tile
-- tileh: vertical size of a tile
function createquads(tilesw, tilesh, tilew, tileh)
    local quads = {}
    for i=0, tilesw-1 do
        for j=0, tilesh do
            local offset = j * tilesw + i
            quads[offset+1] = love.graphics.newQuad(i*tilew, j*tileh, tilew, tileh, tilesw*tilew, tilesh*tileh)
        end
    end
    return quads
end

-- draw one layer of the map using a spritebatch
function drawMap(room, tileset, quads, tilew, tileh)
    local tilesw = tileset:getWidth() / tilew
    local tilesh = tileset:getHeight() / tileh
    local batch = love.graphics.newSpriteBatch(tileset, (screenWidth/tilew)*(screenHeight/tileh))

    for i=1, #room do
        for j=1, #room[1] do
            local t = room[i][j]
            if t ~= 0 then
                batch:addq(quads[t], (j-1)*tilew, (i-1)*tileh)
            end
        end
    end

    love.graphics.draw(batch)
end