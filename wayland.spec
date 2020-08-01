Name:		wayland
Version:	1.18.0
Release:	1
Summary:	Wayland Compositor Infrastructure
License:	MIT
URL:		http://wayland.freedesktop.org/
Source0:	http://wayland.freedesktop.org/releases/%{name}-%{version}.tar.xz

BuildRequires:	gcc chrpath docbook-style-xsl doxygen expat-devel  
BuildRequires:  libxml2-devel libxslt pkgconfig(libffi) xmlto graphviz

Provides:       libwayland-client = %{version}-%{release} libwayland-cursor = %{version}-%{release}  
Obsoletes:      libwayland-client < %{version}-%{release}  libwayland-cursor < %{version}-%{release}  
Provides:       libwayland-egl = %{version}-%{release} libwayland-server = %{version}-%{release}  
Obsoletes:      libwayland-egl < %{version}-%{release} libwayland-server < %{version}-%{release} 

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
Requires:       libwayland-client = %{version}-%{release}
Requires:       libwayland-cursor = %{version}-%{release}
Requires:       libwayland-egl = %{version}-%{release}
Requires:       libwayland-server = %{version}-%{release}
# For upgrade path from F24
Provides:       libwayland-client-devel = %{version}-%{release}
Obsoletes:      libwayland-client-devel < %{version}-%{release}
Provides:       libwayland-cursor-devel = %{version}-%{release}
Obsoletes:      libwayland-cursor-devel < %{version}-%{release}
Provides:       libwayland-server-devel = %{version}-%{release}
Obsoletes:      libwayland-server-devel < %{version}-%{release}
# For upgrade path from F27
Provides:       libwayland-egl-devel = %{version}-%{release}
Obsoletes:      libwayland-egl-devel < %{version}-%{release}
Provides:       mesa-libwayland-egl-devel = %{version}-%{release} mesa-libwayland-egl-devel%{?_isa} = %{version}-%{release}
Obsoletes:      mesa-libwayland-egl-devel < %{version}-%{release} mesa-libwayland-egl-devel%{?_isa} < %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package_help

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

%files
%defattr(-,root,root)
%license COPYING
%{_libdir}/libwayland-*.so.*

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

%files help
%defattr(-,root,root)
%doc README TODO
%{_mandir}/man3/*.3*
%{_datadir}/doc/wayland/


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
