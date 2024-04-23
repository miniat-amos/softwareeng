[Setup]
AppName=LightningBoltTown
AppVersion=1.0
DefaultDirName={pf}\LBT
OutputDir=Output
Compression=lzma2
SolidCompression=yes
DefaultGroupName=LBT
AllowNoIcons=yes
PrivilegesRequired=admin
OutputBaseFilename = LightningBoltTown2Installer

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs ignoreversion
Source: "Scores\*"; DestDir: "{app}\Scores"; Flags: recursesubdirs ignoreversion

[Tasks]
Name: desktopicon; Description: "Create a desktop shortcut";

[Icons]
Name: "{commondesktop}\LightningBoltTown"; Filename: "{app}\main.exe"; \
  WorkingDir: "{app}"; Tasks: desktopicon
Name: "{group}\LightningBoltTown"; Filename: "{app}\main.exe"; \
  WorkingDir: "{app}"

[Dirs]
Name: "{userappdata}\LBT"; Permissions: users-modify
