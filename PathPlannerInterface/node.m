classdef node
    properties
        parent          % Previous node
        children        % Nodes reachable from current node
        location        % Node position in space
        ecefCoords      % Earth-centered, Earth-fixed coordinates of node
        speed           % True Airspeed of aircraft at node
    end
end