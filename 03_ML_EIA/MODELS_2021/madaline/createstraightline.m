% SIMPLE SCRIPT TO CREATE "STRAIGHT LINE DATA" WORKSPACE AND SAVE IT TO "STRAIGHT_LINE.mat"
% Santiago Garcia Arango

N = 50;
entries = zeros(1, N);
desired = zeros(1, N);

for i=1:N
    entries(1, i) = i;
    % Line equation is y=(2*x)
    desired(1, i) = (2*i);
end

% Automatically save the data to the "STRAIGHT_LINE.mat" workspace
save("STRAIGHT_LINE.mat", "entries", "desired");
