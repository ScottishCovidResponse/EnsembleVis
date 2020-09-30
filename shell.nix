with import <nixpkgs> {};
let
  pythonEnv = python38.withPackages (ps: with ps; [
    numpy
    pandas
    h5py
    scikitlearn
  ]);
in mkShell {
  buildInputs = [
    pythonEnv
  ];
  shellHook = ''
    python
  '';
}
