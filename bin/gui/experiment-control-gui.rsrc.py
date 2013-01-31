{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':u'Experiment Control',
          'size':(807, 832),
          'statusBar':1,
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileNew',
                   'label':u'New\tCtrl+N',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileOpen',
                   'label':u'Open\tCtrl+O',
                  },
                  {'type':'MenuItem',
                   'name':'fileSep2',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
             {'type':'Menu',
             'name':'Edit',
             'label':'&Edit',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuEditUndo',
                   'label':'&Undo\tCtrl+Z',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditRedo',
                   'label':'&Redo\tCtrl+Y',
                  },
                  {'type':'MenuItem',
                   'name':'editSep1',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditCut',
                   'label':'Cu&t\tCtrl+X',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditCopy',
                   'label':'&Copy\tCtrl+C',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditPaste',
                   'label':'&Paste\tCtrl+V',
                  },
                  {'type':'MenuItem',
                   'name':'editSep2',
                   'label':'-',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditClear',
                   'label':'Cle&ar\tDel',
                  },
                  {'type':'MenuItem',
                   'name':'menuEditSelectAll',
                   'label':'Select A&ll\tCtrl+A',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'CheckBox', 
    'name':'recordVideo', 
    'position':(220, 600), 
    'backgroundColor':(224, 222, 220, 255), 
    'label':u'Record Video', 
    'toolTip':u'Be aware that recording video uses a lot of memory (+- 500mb per minute)', 
    },

{'type':'StaticText', 
    'name':'playBackSpeedLabel', 
    'position':(334, 125), 
    'backgroundColor':(242, 241, 240, 255), 
    'text':u'Playback Speed:', 
    },

{'type':'StaticBox', 
    'name':'playbackBox', 
    'position':(324, 7), 
    'size':(209, 147), 
    'backgroundColor':(242, 241, 240, 255), 
    'label':u'Debugging', 
    },

{'type':'TextField', 
    'name':'playBackSpeed', 
    'position':(444, 121), 
    'text':u'1.0', 
    },

{'type':'TextField', 
    'name':'filename', 
    'position':(23, 23), 
    'size':(286, -1), 
    'toolTip':u'Double Click to open a file.', 
    },

{'type':'TextField', 
    'name':'serialImu', 
    'position':(170, 80), 
    'size':(151, -1), 
    'editable':False, 
    'toolTip':u'Click to choose the device.', 
    },

{'type':'TextField', 
    'name':'serialAr', 
    'position':(170, 111), 
    'size':(151, -1), 
    'editable':False, 
    'toolTip':u'AR Device - One of the /dev/video devices.', 
    },

{'type':'TextField', 
    'name':'runName', 
    'position':(19, 188), 
    'size':(206, -1), 
    },

{'type':'TextArea', 
    'name':'runNotes', 
    'position':(20, 242), 
    'size':(237, 293), 
    },

{'type':'TextField', 
    'name':'runSubject', 
    'position':(262, 268), 
    'size':(273, -1), 
    },

{'type':'TextField', 
    'name':'runObject', 
    'position':(263, 326), 
    'size':(274, -1), 
    },

{'type':'TextField', 
    'name':'runExperimentType', 
    'position':(265, 379), 
    'size':(272, -1), 
    },

{'type':'StaticText', 
    'name':'runNotesLabel', 
    'position':(19, 218), 
    'backgroundColor':(237, 236, 235, 255), 
    'text':u'Run Notes:', 
    },

{'type':'StaticText', 
    'name':'runSubjectLabel', 
    'position':(263, 245), 
    'backgroundColor':(237, 236, 235, 255), 
    'text':u'Run Subject (Rider,Walker, etc.)', 
    },

{'type':'StaticText', 
    'name':'runObjectLabel', 
    'position':(264, 303), 
    'backgroundColor':(237, 236, 235, 255), 
    'text':u'Run Object (Bicycle Type, Treadmill)', 
    },

{'type':'StaticText', 
    'name':'runExperimentTypeLabel', 
    'position':(266, 359), 
    'backgroundColor':(237, 236, 235, 255), 
    'text':u'Experiment Type (Pertubation etc.)', 
    },

{'type':'CheckBox', 
    'name':'runSuccessful', 
    'position':(270, 410), 
    'backgroundColor':(224, 222, 220, 255), 
    'label':u'Run Successful', 
    },

{'type':'CheckBox', 
    'name':'runCorrupted', 
    'position':(415, 410), 
    'backgroundColor':(224, 222, 220, 255), 
    'label':u'Run Corrupted', 
    },

{'type':'CheckBox', 
    'name':'verboseCheckBox', 
    'position':(340, 60), 
    'backgroundColor':(224, 222, 220, 255), 
    'label':u'Verbose', 
    },

{'type':'ToggleButton', 
    'name':'viewVideo', 
    'position':(340, 85), 
    'size':(184, -1), 
    'backgroundColor':(0, 255, 0, 255), 
    'label':u'View Video', 
    'toolTip':u'If you click and the button flickers, it means the run had no video.', 
    },

{'type':'Button', 
    'name':'openInVitables', 
    'position':(340, 22), 
    'size':(180, 35), 
    'backgroundColor':(0, 220, 244, 255), 
    'label':u'Open in Vitables', 
    },

{'type':'Button', 
    'name':'saveMetaData', 
    'position':(262, 175), 
    'size':(270, 54), 
    'backgroundColor':(0, 220, 244, 255), 
    'label':u'Save Meta Data', 
    },

{'type':'StaticBox', 
    'name':'experimentBox', 
    'position':(9, 154), 
    'size':(529, 391), 
    'backgroundColor':(242, 241, 240, 255), 
    'label':u'Run Information', 
    },

{'type':'TextField', 
    'name':'globalExperimentFeedback', 
    'position':(211, 547), 
    'size':(341, 41), 
    'backgroundColor':(0, 0, 0, 255), 
    'font':{'style': 'bold', 'faceName': u'Ubuntu', 'size': 14}, 
    'foregroundColor':(0, 255, 0, 255), 
    'text':u'Inactive', 
    },

{'type':'ToggleButton', 
    'name':'startStopButton', 
    'position':(10, 547), 
    'size':(193, 139), 
    'backgroundColor':(0, 255, 0, 255), 
    'font':{'faceName': u'Ubuntu', 'family': 'sansSerif', 'size': 42}, 
    'label':u'Start', 
    },

{'type':'StaticText', 
    'name':'runNameLabel', 
    'position':(18, 171), 
    'backgroundColor':(242, 241, 240, 255), 
    'text':u'Run Name', 
    },

{'type':'StaticBox', 
    'name':'h5Filename', 
    'position':(14, 8), 
    'size':(310, 50), 
    'backgroundColor':(242, 241, 240, 255), 
    'label':u'H5 File', 
    },

{'type':'StaticText', 
    'name':'arDeviceLabel', 
    'position':(58, 108), 
    'backgroundColor':(242, 241, 240, 255), 
    'text':u'AR Device', 
    },

{'type':'StaticBox', 
    'name':'imuDeviceBox', 
    'position':(14, 60), 
    'size':(313, 86), 
    'backgroundColor':(242, 241, 240, 255), 
    'label':u'Device setup', 
    },

{'type':'StaticText', 
    'name':'imuDeviceLabel', 
    'position':(58, 85), 
    'backgroundColor':(242, 241, 240, 255), 
    'text':u'IMU Device', 
    },

{'type':'StaticBox', 
    'name':'runListBox', 
    'position':(543, 12), 
    'size':(261, 529), 
    'backgroundColor':(242, 241, 240, 255), 
    'label':u'Runs in file', 
    },

{'type':'List', 
    'name':'runList', 
    'position':(554, 40), 
    'size':(241, 490), 
    'backgroundColor':(242, 241, 240, 255), 
    'items':[], 
    'toolTip':u'Click on a run to view meta information about the run.', 
    },

] # end components
} # end background
] # end backgrounds
} }
