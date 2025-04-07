Name:           sniffnet
Version:        1.3.2
Release:        1
URL:            https://github.com/GyulyVGC/sniffnet
Source0:        https://github.com/GyulyVGC/sniffnet/archive/refs/tags/v%{version}.tar.gz
Summary:        Application to comfortably monitor your network traffic
License:        MIT
BuildRequires:  rustc
BuildRequires:  pkg-config
BuildRequires:  alsa-lib-dev alsa-tools-dev libcap-dev zenity
BuildRequires:  libxcb-dev
BuildRequires:  freetype-dev
BuildRequires:  xclip
BuildRequires:  fontconfig-dev
BuildRequires:  mesa-dev
BuildRequires:  libxkbcommon-dev
BuildRequires:  ncurses-dev
BuildRequires:  expat-dev
BuildRequires:  python3

 
%description
A hardware-accelerated GPU terminal emulator powered by WebGPU.

%prep
%setup -q -n sniffnet-%{version}

%build
unset http_proxy https_proxy no_proxy
export RUSTFLAGS="$RUSTFLAGS -C target-cpu=westmere -C target-feature=+avx -C opt-level=3 -C codegen-units=1 -C panic=abort -Clink-arg=-Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code "
cargo build --release


%install
install -D -m755 target/release/sniffnet %{buildroot}/usr/bin/sniffnet
install -m644 resources/packaging/linux/sniffnet.desktop -pD %{buildroot}/usr/share/applications/sniffnet.desktop
install -m644 resources/logos/raw/icon.png -pD %{buildroot}/usr/share/pixmaps/sniffnet.png
strip %{buildroot}/usr/bin/sniffnet
cp -r /usr/lib64/lib{cap,libpsx}.so.* %{buildroot}/usr/lib64/

%files
%defattr(-,root,root,-)
/usr/bin/sniffnet
/usr/share/applications/sniffnet.desktop
/usr/share/pixmaps/sniffnet.png
/usr/lib64/libcap.so.*
/usr/lib64/libpsx.so.*
