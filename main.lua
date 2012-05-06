-- set the game to blocky interpolation needed now so that all images have it
love.graphics.setDefaultImageFilter("nearest", "nearest")

-- create the map etc.
require("src.map")

-- libraries and utilities.
require("src.util")

-- callback function called once at the start.
-- I try to create everything that can be created at this point.
function love.load()
    -- set up the display
    defaultWidth, defaultHeight = 960, 720
    screenWidth, screenHeight = love.graphics.getMode()

    -- set mouse invisible
    love.mouse.setVisible(false)

    -- we start the game in room 0, will be overwritten when game is loaded.
    currentRoom = 0

    -- init time & timers
    timetot = 0
    timer15, frames15 = 1/15, 0
    timer30, frames30 = 1/30, 0
    timer60, frames60 = 1/60, 0
end

-- callback function called each frame, before the draw.
-- this is a long function due to different stuff that doesn't really need to
-- be moved.
function love.update(dt)
    ----------------------------------------------- TIMER PREP ----------------
    -- do some check for tripped timers.
    if timer15 < 0 then
        timer15 = 1/15
        frames15 = frames15 + 1
    end
    if timer30 < 0 then
        timer30 = 1/30
        frames30 = frames30 + 1
    end
    if timer60 < 0 then
        timer60 = 1/60
        frames60 = frames60 + 1
    end
    -- if the dt is unusually high, set it to 1/60
    if dt >= 1/10 then dt = 1/60 end

    ----------------------------------------------- RESIDENT INPUT CHECKS -----
    -- quit when you press escape
    if love.keyboard.isDown("escape") then
        love.event.push("quit")
    end

    -- toggle fullscreen on alt+enter
    if (love.keyboard.isDown("lalt") or love.keyboard.isDown("ralt")) and love.keyboard.isDown("return") then
        local _, _, fullscreen = love.graphics.getMode()
	if fullscreen then
            love.graphics.setMode(defaultWidth, defaultHeight, false, true, 0)
            screenWidth, screenHeight = love.graphics.getMode()
	else
            love.graphics.setMode(0, 0, false, true, 0)
            screenWidth, screenHeight = love.graphics.getMode()
            love.graphics.setMode(screenWidth, screenHeight, true, true, 0)
        end
        dt = 0  -- this can take a while, act as if no time has passed at all
    end

    ----------------------------------------------- GAMESTATES ----------------


    ----------------------------------------------- ADJUST TIMERS -------------
    -- adjust all the timers
    timetot = timetot + dt
    timer15 = timer15 - dt
    timer30 = timer30 - dt
    timer60 = timer60 - dt
    delta = dt
end

-- callback function called once per frame
function love.draw()
    -- scale the screen.
    if (screenWidth ~= defaultWidth) or (screenHeight ~= defaultHeight) then
        local scalefactor = screenHeight/defaultHeight
        love.graphics.translate((screenWidth-scalefactor*defaultWidth)/2, 0)
        love.graphics.scale(scalefactor, scalefactor)
    end

    love.graphics.setColor(255, 255, 255)
    love.graphics.setBackgroundColor(0, 0, 0)

    -- draw the background
    drawMap(map[currentRoom]:layer0(), 
        map[currentRoom]:tileset(), 
        map[currentRoom]:quads(),
        60, 60)

    -- draw the middle layer
    drawMap(map[currentRoom]:layer1(), 
        map[currentRoom]:tileset(), 
        map[currentRoom]:quads(),
        60, 60)

    -- draw the foreground
    drawMap(map[currentRoom]:layer2(), 
        map[currentRoom]:tileset(), 
        map[currentRoom]:quads(),
        60, 60)

    -- debug out goes here.
    -- love.graphics.setColor(0, 0, 255)
    -- love.graphics.print("derp", 10, 10)
end
