{
  description = "dccex development environment";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      forEachSupportedSystem =
        f:
        nixpkgs.lib.genAttrs supportedSystems (
          system:
          f {
            pkgs = nixpkgs.legacyPackages.${system};
          }
        );
    in
    {
      devShells = forEachSupportedSystem (
        { pkgs }:
        {
          default = pkgs.mkShell {
            # Note: uv does not have a package, and does not seem to play well
            # with nix from my research so it needs to be installed manually system wide.
            packages = with pkgs; [
              fish
              just
              just-lsp
              nil
            ];

            shellHook = ''
              # Enable fish
              if [ -z "$IN_DCCEX_SHELL" ]; then
                export IN_DCCEX_SHELL=1
                exec fish
              fi
            '';
          };
        }
      );
    };
}
