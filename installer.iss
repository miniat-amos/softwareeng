[Setup]
AppName=LightningBoltTown
AppVersion=1.0
DefaultDirName={pf}\LBT
OutputDir=Output
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs ignoreversion
Source: "Scores\*"; DestDir: "{app}\Scores"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{commondesktop}\LightningBoltTown"; Filename: "{app}\main.exe"; \
  WorkingDir: "{app}"