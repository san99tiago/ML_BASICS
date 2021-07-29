%ESTA FUNCION PERMITE MODIFICAR UNA FIGURA YA EXISTENTE Y PONERLA LINDA
%Santiago Garcia Arango
%-----------------------------------------------------------------------------------------
% COMO USAR?
%Al graficar un comando de graficas como "step()", "bode()", en la linea inmediata...
%...despues, agregamos esta funcion, para modificarle los atributos importantes a ...
%...el color, las lineas, los tamannos y que la grafica quede mas bonita (inmediatamente)

%Parametros:
%nombre_grafica --> Agregar el nombre que queramos que tenga el titulo de la grafica
%tipo_grafica   --> Agregamos el string asociado a la grafica realizada, por ejemplo:
%                   "step" , "bode" , "" (segun sea el caso de la grafica)
%-----------------------------------------------------------------------------------------

function [] = PRETTY_GRAPH(nombre_grafica, tipo_grafica )
    
    %Validamos si usuario ingreso ambos parametros, solo el primero, o ninguno...
    switch nargin
        case (0)
            nombre_grafica = "";
            tipo_grafica = "";
        case (1)
            tipo_grafica = "";
    end


    %Agregamos titulo a la figura (congruente con el parametro de entrada)
    title(nombre_grafica);
    %Agregamos el grid para visualizar mejor la curva y sus valores clave
    grid on
    %Creamos un "current figure handle", para editar opciones deseadas de figura
    fig = gcf;
    %Cambiamos color (en este caso a azul)
    fig.Color = [0.2 1 1];
    %Agregamos titulo de la figura
    fig.Name = nombre_grafica;
    %Creamos un "current axis handle", para editar opciones deseadas de ejes
    ax = gca;
    %Cambiamos tamanno letra de los ejes 
    ax.FontSize = 12;
    
    %Segun el tipo de figura, cambiamos tamanno linea a "2"
    if (tipo_grafica=="bode")       
        %Cambiamos tamanno de grosor de linea por 2
        set(findall(gcf,'type','line'),'linewidth',2)
    elseif (tipo_grafica=="step")
        %Buscamos lineas de curva que posee la figura
        hline=findobj(fig,'Type','line','Tag','Curves');
        %Cambiamos grosor de la linea de la figura
        hline(1).LineWidth = 2;  
    end
    
    %Redimensionamos y relocalizamos figura (cambiar segun tamanno pantalla actual)
    set(gcf,'Position',[10 250 550 350])
    
        
    %Permitimos espera, por si se desean agregar mas graficas a esta figura
    hold on