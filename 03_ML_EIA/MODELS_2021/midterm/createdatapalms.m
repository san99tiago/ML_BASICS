% SIMPLE SCRIPT TO CREATE "PALMS" WORKSPACE AND SAVE IT TO "PALMS.mat"
% Santiago Garcia Arango
%
% ENTRIES:
%
%     <------------ collection1 ------------><----- collection2 -----><--- cn --->
%       d1  d2  d3  d4  d5  d6  d7  d8  d9  d10  d11  d12  d13  d14 ...  dn-1  dn
%     -----------------------------------------------------------------------------
%  x1 |   |   |   |   |   |   |   |   |   |    |    |    |    |    | .. |     |    | 
%  x2 |   |   |   |   |   |   |   |   |   |    |    |    |    |    | .. |     |    |
%  x3 |   |   |   |   |   |   |   |   |   |    |    |    |    |    | .. |     |    |
%  x4 |   |   |   |   |   |   |   |   |   |    |    |    |    |    | .. |     |    |
%     -----------------------------------------------------------------------------
%
%
% DESIRED:
%     <------------ collection1 ------------><----- collection2 -----><--- cn --->
%       d1  d2  d3  d4  d5  d6  d7  d8  d9  d10  d11  d12  d13  d14 ...  dn-1  dn
%     ---------------------------------------------------------------------------
%  y1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  1 |  0 |  0 |  0 |  0 | .. | 0 |  0 |
%  y2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 |  1 |  1 |  1 |  1 | .. | 0 |  0 |
%  y3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 |  0 |  0 |  0 |  0 | .. | 0 |  0 |
%  y4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 |  0 |  0 |  0 |  0 | .. | 0 |  0 |
%  y5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 |  0 |  0 |  0 |  0 | .. | 0 |  0 |
%  y6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  0 |  0 |  0 |  0 |  0 | .. | 1 |  1 |
%     ---------------------------------------------------------------------------


% Important variables to fill input data
N = 60;  % Total data collected  for all palms
data_collection_size = 15;  % Amount of data per type of palm
types_of_entries = 4;  % Amount of entries per data taken
types_of_outputs = 4;  % Amount of "classifications" for the desired outputs

% Initialize entries and desired
entries = zeros(types_of_entries, N);
desired = zeros(types_of_outputs, N);

% Create entries matrix
current_mean_value = 1;
central_value = 1;
counter = 0;
limit_1 = 4;
for j=1:N
    if (counter == data_collection_size)
        counter = 0;
        current_mean_value = current_mean_value + 1;
    end
    
    if (current_mean_value == limit_1)
        current_mean_value = 1;
    end
    
    for i=1:types_of_entries
        entries(i, j) = randi([current_mean_value, current_mean_value + 1]);
    end
    counter = counter + 1;
end

% Create desired matrix
current_category = 1;
counter = 0;
for j=1:N
    if (counter == data_collection_size)
        counter = 0;
        current_category = current_category + 1;
    end
    desired(current_category, j) = 1;
    counter = counter + 1;
end

% Automatically save the data to the "PALMS.mat" workspace
save("PALMS.mat", "entries", "desired");

