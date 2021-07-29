% SIMPLE SCRIPT TO CREATE "BIN-DEC DECODER" WORKSPACE AND SAVE IT TO "BIN_DEC.mat"
% Santiago Garcia Arango

entries = [
    0, 0, 0, 0, 1, 1, 1, 1;
    0, 0, 1, 1, 0, 0, 1, 1;
    0, 1, 0, 1, 0, 1, 0, 1];
    
desired = [0, 1, 2, 3, 4, 5, 6, 7];

% Automatically save the data to the "BIN_DEC.mat" workspace
save("BIN_DEC.mat", "entries", "desired");
