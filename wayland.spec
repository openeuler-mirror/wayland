Name:           wayland
Version:        1.16.0
Release:        1%{?dist}
Summary:        Wayland Compositor Infrastructure

License:        MIT
URL:            http://wayland.freedesktop.org/
Source0:        http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  chrpath
BuildRequires:  docbook-style-xsl
BuildRequires:  doxygen
BuildRequires:  expat-devel
BuildRequires:  graphviz
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  pkgconfig(libffi)
BuildRequires:  xmlto

Provides:       libwayland-client
Obsoletes:      libwayland-client

Provides:       libwayland-cursor
Obsoletes:      libwayland-cursor

Provides:       libwayland-egl
Obsoletes:      libwayland-egl

Provides:       libwayland-server
Obsoletes:      libwayland-server

Provides:       mesa-libwayland-egl
Obsoletes:      mesa-libwayland-egl

%description
Wayland is a protocol for a compositor to talk to its clients as well as a C
library implementation of that protocol. The compositor can be a standalone
display server running on Linux kernel modesetting and evdev input devices,
an X application, or a wayland client itself. The clients can be traditional
applications, X servers (rootless or fullscreen) or other display servers.

%package        devel
Summary:        Development files for %{name}
Requires:       libwayland-client
Requires:       libwayland-cursor
Requires:       libwayland-egl
Requires:       libwayland-server

Provides:       libwayland-client-devel = %{version}-%{release}
Obsoletes:      libwayland-client-devel < 1.11.91
Provides:       libwayland-cursor-devel = %{version}-%{release}
Obsoletes:      libwayland-cursor-devel < 1.11.91
Provides:       libwayland-server-devel = %{version}-%{release}
Obsoletes:      libwayland-server-devel < 1.11.91

Provides:       libwayland-egl-devel = %{version}-%{release}
Provides:       mesa-libwayland-egl-devel = %{version}-%{release}
Provides:       mesa-libwayland-egl-devel%{?_isa} = %{version}-%{release}
Obsoletes:      mesa-libwayland-egl-devel < 18.1.0

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package help
Summary: Wayland development documentation
BuildArch:  noarch
Provides:   wayland-doc
Obsoletes:  wayland-doc

%description help
Wayland development documentation

%prep
%autosetup -p1

%build
%configure --disable-static --enable-documentation
make %{?_smp_mflags}

%install
%make_install

find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

chrpath -d $RPM_BUILD_ROOT%{_libdir}/libwayland-cursor.so

%check
mkdir -m 700 tests/run
XDG_RUNTIME_DIR=$PWD/tests/run 
make check || \
{ rc=$?; cat test-suite.log; exit $rc; }

%files
%license COPYING
%{_libdir}/libwayland-client.so.0*
%{_libdir}/libwayland-cursor.so.0*
%{_libdir}/libwayland-egl.so.1*
%{_libdir}/libwayland-server.so.0*

%files devel
%{_bindir}/wayland-scanner
%{_includedir}/wayland-*.h
%{_libdir}/pkgconfig/wayland-*.pc
%{_libdir}/libwayland-*.so
%{_datadir}/aclocal/wayland-scanner.m4
%dir %{_datadir}/wayland
%{_datadir}/wayland/wayland-scanner.mk
%{_datadir}/wayland/wayland.xml
%{_datadir}/wayland/wayland.dtd
%{_mandir}/man3/*.3*

%files help
%doc README TODO
%{_datadir}/doc/wayland/

%changelog
* Thu Sep 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:6.02-5
- Package init
