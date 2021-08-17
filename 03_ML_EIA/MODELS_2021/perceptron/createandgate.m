% SIMPLE SCRIPT TO CREATE "AND-GATE" WORKSPACE AND SAVE IT TO "AND.mat"
% Santiago Garcia Arango

entries = [0, 1, 0, 1; 0, 0, 1, 1];
desired = [0, 0, 0, 1];

% Automatically save the data to the "AND.mat" workspace
save("AND.mat", "entries", "desired");
