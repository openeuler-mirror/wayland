Name:		wayland
Version:	1.17.0
Release:	2
Summary:	Wayland Compositor Infrastructure
License:	MIT
URL:		http://wayland.freedesktop.org/
Source0:	http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:	gcc chrpath docbook-style-xsl doxygen expat-devel  
BuildRequires:  libxml2-devel libxslt libffi-devel xmlto graphviz

Provides:       libwayland-client libwayland-cursor libwayland-egl
Obsoletes:      libwayland-client libwayland-cursor libwayland-egl

Provides:       libwayland-server mesa-libwayland-egl
Obsoletes:      libwayland-server mesa-libwayland-egl

%description
Wayland is a protocol for a compositor to talk to its clients as 
well as a C library implementation of that protocol. The 
compositor can be a standalone display server running on Linux 
kernel modesetting and evdev input devices, an X application, or 
a wayland client itself. The clients can be traditional 
applications, X servers (rootless or fullscreen) or other display 
servers.

Part of the Wayland project is also the Weston reference 
implementation of a Wayland compositor. Weston can run as an X 
client or under Linux KMS and ships with a few demo clients. The 
Weston compositor is a minimal and fast compositor and is 
suitable for many embedded and mobile use cases.

%package        devel
Summary:        Header files for wayland
Requires:       %{name} = %{version}-%{release}

Provides:       libwayland-client-devel libwayland-cursor-devel
Obsoletes:      libwayland-client-devel libwayland-cursor-devel

Provides:       libwayland-server-devel libwayland-egl-devel
Obsoletes:      libwayland-server-devel libwayland-egl-devel

Provides:       mesa-libwayland-egl-devel mesa-libwayland-egl-devel%{?_isa}
Obsoletes:      mesa-libwayland-egl-devel 

%description    devel
Header files for wayland.

%package        help
Summary:        Documents for wayland
BuildArch:      noarch
Requires:       man info
Provides:       wayland-doc
Obsoletes:      wayland-doc

%description    help 
Man pages and other related documents for wayland

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure  --enable-documentation
%make_build

%install
%make_install
%delete_la

chrpath -d %{buildroot}%{_libdir}/libwayland-cursor.so

%check
mkdir -m 700 tests/run
XDG_RUNTIME_DIR=$PWD/tests/run 
make check || \
{ rc=$?; cat test-suite.log; exit $rc; }

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/libwayland-*.so.*

%files          devel
%defattr(-,root,root)
%{_bindir}/wayland-scanner
%{_libdir}/libwayland-*.so
%{_libdir}/pkgconfig/wayland-*.pc
%{_includedir}/wayland-*.h
%{_datadir}/wayland/*
%{_datadir}/aclocal/*

%files          help
%defattr(-,root,root)
%doc README TODO
%{_mandir}/man3/*
%{_datadir}/doc/wayland/

%changelog
* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.17.0-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:delete the isa in obsoletes

* Fri Oct 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.17.0-1
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:update to 1.17.0

* Thu Sep 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:6.02-5
- Package init
