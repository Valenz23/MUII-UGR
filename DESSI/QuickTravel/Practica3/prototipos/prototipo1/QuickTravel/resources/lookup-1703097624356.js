(function(window, undefined) {
  var dictionary = {
    "4e39cbc2-ef25-4ce0-80c4-17b08f574a9c": "contactos",
    "e4a7ac8c-d008-465a-a5ba-dad5ef0f4d6d": "inicio",
    "7699c6f4-e99e-4163-8b56-5383848d89df": "registro",
    "d12245cc-1680-458d-89dd-4f0d7fb22724": "Loguearse",
    "d471e6be-722b-4289-a4a6-22a129a65862": "error_login",
    "d639823a-add8-4ab5-8c0f-1f460b7e886c": "perfil_usuario",
    "1babc1b0-ad6d-49e7-a540-677bde277f9b": "perfil_localizacion",
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