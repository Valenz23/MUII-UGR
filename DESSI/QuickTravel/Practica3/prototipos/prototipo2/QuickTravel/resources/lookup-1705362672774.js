(function(window, undefined) {
  var dictionary = {
    "02e86551-4e38-4404-8e4f-81367399085d": "crear ruta 1",
    "e4a7ac8c-d008-465a-a5ba-dad5ef0f4d6d": "inicio",
    "761e17d9-4016-42d3-86a9-92aef0fba110": "editar ruta 2",
    "91d52cea-b132-4968-be2f-8c614f78dc4b": "localizacion - DATOS_editar ruta",
    "76775d35-8df5-4014-b952-059d98a7145b": "crear ruta 2",
    "1babc1b0-ad6d-49e7-a540-677bde277f9b": "menu - perfil_localizacion [A]",
    "4e39cbc2-ef25-4ce0-80c4-17b08f574a9c": "contactos",
    "bd48995b-8bc6-4d41-8fab-7b7e7c5cc426": "localizacion - DATOS_normal",
    "6c461711-eacb-4ed1-b333-9b819cab482e": "localizacion - RESEÑAS_normal",
    "87a3a7ab-b815-47eb-a4f8-41f692128f10": "crear ruta 4",
    "a9728240-1718-464b-a2dd-56afe2f18758": "editar ruta 1",
    "2d9938d3-2b8b-4744-9266-62aa86841c4d": "inicio con RUTA",
    "b85dbafa-dce5-4914-9bee-803e3cc20476": "crear ruta 3",
    "7699c6f4-e99e-4163-8b56-5383848d89df": "registro",
    "b3e60a04-98c3-4a42-b91c-e0f5f994cc4d": "localizacion - RESEÑAS_editar ruta",
    "ddd62775-3730-4128-8655-17f96ae97535": "menu - ver mis rutas",
    "d12245cc-1680-458d-89dd-4f0d7fb22724": "Loguearse",
    "d471e6be-722b-4289-a4a6-22a129a65862": "error_login",
    "d639823a-add8-4ab5-8c0f-1f460b7e886c": "menu - perfil_usuario [A]",
    "8002115f-7bef-4df3-997f-091229ff38d6": "inicio FILTRO",
    "f39803f7-df02-4169-93eb-7547fb8c961a": "Template 1",
    "bb8abf58-f55e-472d-af05-a7d1bb0cc014": "default"
  };

  var uriRE = /^(\/#)?(screens|templates|masters|scenarios)\/(.*)(\.html)?/;
  window.lookUpURL = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, url;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      url = folder + "/" + canvas;
    }
    return url;
  };

  window.lookUpName = function(fragment) {
    var matches = uriRE.exec(fragment || "") || [],
        folder = matches[2] || "",
        canvas = matches[3] || "",
        name, canvasName;
    if(dictionary.hasOwnProperty(canvas)) { /* search by name */
      canvasName = dictionary[canvas];
    }
    return canvasName;
  };
})(window);