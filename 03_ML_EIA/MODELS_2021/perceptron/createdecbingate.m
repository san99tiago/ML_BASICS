% SIMPLE SCRIPT TO CREATE "DEC-BIN" WORKSPACE AND SAVE IT TO "DEC_BIN.mat"
% Santiago Garcia Arango

entries = [0, 1, 2, 3, 4, 5, 6, 7];
desired = [0, 0, 0, 0, 1, 1, 1, 1;
           0, 0, 1, 1, 0, 0, 1, 1;
           0, 1, 0, 1, 0, 1, 0, 1];

% Automatically save the data to the "DEC_BIN.mat" workspace
save("DEC_BIN.mat", "entries", "desired");
