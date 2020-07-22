Name:		wayland
Version:	1.18.0
Release:	1
Summary:	Wayland Compositor Infrastructure
License:	MIT
URL:		http://wayland.freedesktop.org/
Source0:	http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:	gcc chrpath docbook-style-xsl doxygen expat-devel  
BuildRequires:  libxml2-devel libxslt pkgconfig(libffi) xmlto graphviz

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
Summary:        Development files for %{name}
Requires:       libwayland-client%{?_isa} = %{version}-%{release}
Requires:       libwayland-cursor%{?_isa} = %{version}-%{release}
Requires:       libwayland-egl%{?_isa} = %{version}-%{release}
Requires:       libwayland-server%{?_isa} = %{version}-%{release}
# For upgrade path from F24
Provides:       libwayland-client-devel = %{version}-%{release}
Provides:       libwayland-cursor-devel = %{version}-%{release}
Provides:       libwayland-server-devel = %{version}-%{release}
# For upgrade path from F27
Provides:       libwayland-egl-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Wayland development documentation
BuildArch: noarch
%description doc
Wayland development documentation

%package -n libwayland-client
Summary: Wayland client library
%description -n libwayland-client
Wayland client library

%package -n libwayland-cursor
Summary: Wayland cursor library
%description -n libwayland-cursor
Wayland cursor library

%package -n libwayland-egl
Summary: Wayland egl library
%description -n libwayland-egl
Wayland egl library

%package -n libwayland-server
Summary: Wayland server library
%description -n libwayland-server
Wayland server library

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure  --disable-static --enable-documentation
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

%files doc
%doc README TODO
%{_datadir}/doc/wayland/

%files -n libwayland-client
%license COPYING
%{_libdir}/libwayland-client.so.0*

%files -n libwayland-cursor
%license COPYING
%{_libdir}/libwayland-cursor.so.0*

%files -n libwayland-egl
%license COPYING
%{_libdir}/libwayland-egl.so.1*

%files -n libwayland-server
%license COPYING
%{_libdir}/libwayland-server.so.0*


%changelog
* Fri Jul 17 2020 chengguipeng <chenguipeng1@huawei.com> - 1.18.0-1
- upgrade to 1.18.0-1

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
