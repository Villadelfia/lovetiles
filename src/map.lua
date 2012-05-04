require("src.Room")
require("src.util")

-- load the tilesets
tiles = {}
tiles["normal"] = love.graphics.newImage("images/tiles.png")

-- create the quads for the tilesets
quads = {}
quads["normal"] = createquads(12, 9, 60, 60)

-- create the map
map = {}

-- require all the rooms
files = love.filesystem.enumerate("src/rooms")
for _, f in ipairs(files) do
    if f:find(".lua") then
        require("src.rooms."..f:sub(0, -5))
    end
end