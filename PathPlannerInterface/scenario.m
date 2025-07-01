classdef scenario
    %SCENARIO Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        zones       % Restricted/limited regions of space
        goals       % Matrix of lat, long, alt for task locations
        startPos    % start position of each platform
        units       % indicates unit system
        avoid       % integer array indicating zone restrictions
        bases       % lat, long, alt for base locations
    end
end

