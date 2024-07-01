jQuery("#simulation")
  .on("click", ".s-87a3a7ab-b815-47eb-a4f8-41f692128f10 .click", function(event, data) {
    var jEvent, jFirer, cases;
    if(jimUtil.isAlternateModeActive()) return;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    event.data = data;
    jFirer = jEvent.getEventFirer();
    if(jFirer.is("#s-Hotspot_6")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimShow",
                  "parameter": {
                    "target": [ "#s-Group_1" ]
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimNavigation",
                  "parameter": {
                    "target": "screens/b85dbafa-dce5-4914-9bee-803e3cc20476",
                    "transition": {
                      "type": "fade",
                      "duration": 700
                    }
                  },
                  "exectype": "timed",
                  "delay": 1000
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Hotspot_7")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimNavigation",
                  "parameter": {
                    "target": "screens/b85dbafa-dce5-4914-9bee-803e3cc20476",
                    "transition": {
                      "type": "fade",
                      "duration": 700
                    }
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Paragraph_7")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimHide",
                  "parameter": {
                    "target": [ "#s-Group_8" ]
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Paragraph_9")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimNavigation",
                  "parameter": {
                    "target": "screens/e4a7ac8c-d008-465a-a5ba-dad5ef0f4d6d",
                    "transition": {
                      "type": "fade",
                      "duration": 700
                    }
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Hotspot_1")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimShow",
                  "parameter": {
                    "target": [ "#s-Group_8" ]
                  },
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    }
  })
  .on("drag", ".s-87a3a7ab-b815-47eb-a4f8-41f692128f10 .drag", function(event, data) {
    var jEvent, jFirer, cases;
    if(jimUtil.isAlternateModeActive()) return;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    event.data = data;
    jFirer = jEvent.getDirectEventFirer(this);
    if(jFirer.is("#s-Hotspot_2")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimMove",
                  "parameter": {
                    "target": [ "#s-Group_4" ],
                    "top": {
                      "type": "movewithcursor",
                      "value": ""
                    },
                    "left": {
                      "type": "movewithcursor",
                      "value": ""
                    },
                    "containment": false
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeCursor",
                  "parameter": {
                    "type": "move"
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "target": [ "#s-87a3a7ab-b815-47eb-a4f8-41f692128f10 #s-Rectangle_4" ],
                    "attributes": {
                      "filter": "none"
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeCursor",
                  "parameter": {
                    "type": "default"
                  },
                  "exectype": "timed",
                  "delay": 600
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Hotspot_3")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimMove",
                  "parameter": {
                    "target": [ "#s-Group_5" ],
                    "top": {
                      "type": "movewithcursor",
                      "value": ""
                    },
                    "left": {
                      "type": "movewithcursor",
                      "value": ""
                    },
                    "containment": false
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeCursor",
                  "parameter": {
                    "type": "move"
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "target": [ "#s-87a3a7ab-b815-47eb-a4f8-41f692128f10 #s-Rectangle_5" ],
                    "attributes": {
                      "filter": " drop-shadow(-1.8369701987210297E-16px 3.0px 3px rgba(0,0,0,0.2))"
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeCursor",
                  "parameter": {
                    "type": "default"
                  },
                  "exectype": "timed",
                  "delay": 600
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Hotspot_4")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimMove",
                  "parameter": {
                    "target": [ "#s-Group_6" ],
                    "top": {
                      "type": "movewithcursor",
                      "value": ""
                    },
                    "left": {
                      "type": "movewithcursor",
                      "value": ""
                    },
                    "containment": false
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeCursor",
                  "parameter": {
                    "type": "move"
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "target": [ "#s-87a3a7ab-b815-47eb-a4f8-41f692128f10 #s-Rectangle_6" ],
                    "attributes": {
                      "filter": " drop-shadow(-1.8369701987210297E-16px 3.0px 3px rgba(0,0,0,0.2))"
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeCursor",
                  "parameter": {
                    "type": "default"
                  },
                  "exectype": "timed",
                  "delay": 600
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Hotspot_5")) {
      cases = [
        {
          "blocks": [
            {
              "actions": [
                {
                  "action": "jimMove",
                  "parameter": {
                    "target": [ "#s-Group_7" ],
                    "top": {
                      "type": "movewithcursor",
                      "value": ""
                    },
                    "left": {
                      "type": "movewithcursor",
                      "value": ""
                    },
                    "containment": false
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeCursor",
                  "parameter": {
                    "type": "move"
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "target": [ "#s-87a3a7ab-b815-47eb-a4f8-41f692128f10 #s-Rectangle_7" ],
                    "attributes": {
                      "filter": " drop-shadow(-1.8369701987210297E-16px 3.0px 3px rgba(0,0,0,0.2))"
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeCursor",
                  "parameter": {
                    "type": "default"
                  },
                  "exectype": "timed",
                  "delay": 600
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    }
  })
  .on("dragend", ".s-87a3a7ab-b815-47eb-a4f8-41f692128f10 .drag", function(event, data) {
    jimEvent(event).jimRestoreDrag(jQuery(this));
  })
  .on("dragend", ".s-87a3a7ab-b815-47eb-a4f8-41f692128f10 .dragend", function(event, data) {
    var jEvent, jFirer, cases;
    if(jimUtil.isAlternateModeActive()) return;
    if(data === undefined) { data = event; }
    jEvent = jimEvent(event);
    event.data = data;
    jFirer = jEvent.getDirectEventFirer(this);
    if(jFirer.is("#s-Hotspot_2")) {
      cases = [
        {
          "blocks": [
            {
              "condition": (jimUtil.intersect(jQuery.Event(event), jEvent.getEventTarget("#s-Group_4"))),
              "actions": [
                {
                  "action": "jimInsert",
                  "parameter": {
                    "target": [ "#s-Group_4" ],
                    "parent": "#s-Panel_1"
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "target": [ "#s-87a3a7ab-b815-47eb-a4f8-41f692128f10 #s-Rectangle_4" ],
                    "attributes": {
                      "filter": " drop-shadow(-1.8369701987210297E-16px 3.0px 3px rgba(0,0,0,0.2))"
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Hotspot_3")) {
      cases = [
        {
          "blocks": [
            {
              "condition": (jimUtil.intersect(jQuery.Event(event), jEvent.getEventTarget("#s-Group_5"))),
              "actions": [
                {
                  "action": "jimInsert",
                  "parameter": {
                    "target": [ "#s-Group_5" ],
                    "parent": "#s-Panel_1"
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "target": [ "#s-87a3a7ab-b815-47eb-a4f8-41f692128f10 #s-Rectangle_5" ],
                    "attributes": {
                      "filter": " drop-shadow(7.071067811865475px 7.0710678118654755px 5px rgba(64,64,64,0.0))"
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Hotspot_4")) {
      cases = [
        {
          "blocks": [
            {
              "condition": (jimUtil.intersect(jQuery.Event(event), jEvent.getEventTarget("#s-Group_6"))),
              "actions": [
                {
                  "action": "jimInsert",
                  "parameter": {
                    "target": [ "#s-Group_6" ],
                    "parent": "#s-Panel_1"
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "target": [ "#s-87a3a7ab-b815-47eb-a4f8-41f692128f10 #s-Rectangle_6" ],
                    "attributes": {
                      "filter": " drop-shadow(7.071067811865475px 7.0710678118654755px 5px rgba(64,64,64,0.0))"
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    } else if(jFirer.is("#s-Hotspot_5")) {
      cases = [
        {
          "blocks": [
            {
              "condition": (jimUtil.intersect(jQuery.Event(event), jEvent.getEventTarget("#s-Group_7"))),
              "actions": [
                {
                  "action": "jimInsert",
                  "parameter": {
                    "target": [ "#s-Group_7" ],
                    "parent": "#s-Panel_1"
                  },
                  "exectype": "serial",
                  "delay": 0
                },
                {
                  "action": "jimChangeStyle",
                  "parameter": [ {
                    "target": [ "#s-87a3a7ab-b815-47eb-a4f8-41f692128f10 #s-Rectangle_7" ],
                    "attributes": {
                      "filter": " drop-shadow(7.071067811865475px 7.0710678118654755px 5px rgba(64,64,64,0.0))"
                    }
                  } ],
                  "exectype": "serial",
                  "delay": 0
                }
              ]
            }
          ],
          "exectype": "serial",
          "delay": 0
        }
      ];
      jEvent.launchCases(cases);
    }
  })
  .on("dragend", ".s-87a3a7ab-b815-47eb-a4f8-41f692128f10 .drag", function(event, data) {
    var id = data.drag.id;
    if(id.startsWith("r")){
    	var numR = id.match(/\d+/)[0];
    	id = id.replace("r"+numR+"_",'');
    }
    if(id.startsWith("s-"))
      jimEvent(event).jimDestroyDrag(jQuery(this));
  });