Room = {}

Room.new = function(args)
    -- private members
    local self = {}
    layer0 = args.layer0
    layer1 = args.layer1
    layer2 = args.layer2
    clippingmask = args.clippingmask
    tileset = args.tileset
    quads = args.quads

    -- public functions
    self.layer0 = function() return layer0 end
    self.layer1 = function() return layer1 end
    self.layer2 = function() return layer2 end
    self.tileset = function() return tileset end
    self.clippingmask = function() return clippingmask end
    self.quads = function() return quads end
	
    return self
end