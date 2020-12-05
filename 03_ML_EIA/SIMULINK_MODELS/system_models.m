% MODELS FOR SYSTEMS IDENTIFICATION
% Sennales del sistema
yd = out.ST(:,2);
u = out.ST(:,1);
k = 1:1:size(yd);

subplot(4,1,1)
plot(k, u, "r", k, yd, "b");
hold on

% ---------------------------------------
% Modelo Autoregresivo con Entrada Exogena

% Create system simulation matrix for the dynamic system
data = idata(yd,u, 0.01);
subplot(4,1,2);
autocorr(yd,40);
subplot(4,1,3);
parcorr(yd,40);

% Create ARX model

% setpoint_delays = 1;
yarx = arx(data, [4,1,0])

