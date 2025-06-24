[Setup]
AppId={{15FC6141-4E3A-41D2-8E79-C8633AF0FF5A}} 
AppName=SchedMed
AppVersion=1.0
DefaultDirName={pf}\SchedMed
DefaultGroupName=SchedMed
OutputDir=Output
OutputBaseFilename=SchedMedSetup
SetupIconFile=deployed\icon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "deployed\SchedMed.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "deployed\icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "deployed\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\SchedMed"; Filename: "{app}\SchedMed.exe"
Name: "{group}\{cm:UninstallProgram,SchedMed}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\SchedMed"; Filename: "{app}\SchedMed.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\SchedMed.exe"; Description: "{cm:LaunchProgram,SchedMed}"; Flags: nowait postinstall skipifsilent
