%define         git_commit 1a1bda4

%define major 0
%define libname %mklibname nm-qt %{major}
%define devname %mklibname -d nm-qt

Name:           libnm-qt
Version:        0.9.8
Release:        2.20130613git%{git_commit}%{?dist}
Summary:        Qt-only wrapper for NetworkManager DBus API
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://projects.kde.org/projects/extragear/libs/libnm-qt
# Package from git snapshots, create example:
# git clone git://anongit.kde.org/libnm-qt.git
# cd libnm-qt
# git archive --prefix=libnm-qt-%{version}/ master | bzip2 > ../%{name}-%{version}-git%{git_commit}.tar.bz2
Source0:        %{name}-%{version}-git%{git_commit}.tar.bz2

BuildRequires:  cmake >= 2.6
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  libmm-qt-devel >= 0.6.0
BuildRequires:  pkgconfig(NetworkManager) >= 0.9.8
BuildRequires:  pkgconfig(libnm-glib) pkgconfig(libnm-util)

Requires:  NetworkManager >= 0.9.8

%description
Qt library for NetworkManager

%package -n %{libname}
Summary:        Qt-only wrapper for NetworkManager DBus API
Group:          System/Libraries

%description -n %{libname}
Qt library for NetworkManager


%package -n %{devname}
Summary: Development files for %{name}
Group:   Development/C++
Requires: %{libname} = %{version}-%{release}

%description -n %{devname}
Qt libraries and header files for developing applications
that use NetworkManager

%prep
%setup -qn %{name}-%{version}-git%{git_commit}

%build
%cmake
%make

%install
make install/fast  DESTDIR=%{buildroot} -C build

%files -n %{libname}
%{_libdir}/libNetworkManagerQt.so.0*

%files -n %{devname}
%{_libdir}/pkgconfig/NetworkManagerQt.pc
%{_libdir}/libNetworkManagerQt.so
%{_includedir}/NetworkManagerQt/
