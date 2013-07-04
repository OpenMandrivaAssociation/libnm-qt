%define git_commit 1a1bda4
%define snapshot 20130613

%define major 0
%define libname %mklibname nm-qt %{major}
%define devname %mklibname -d nm-qt

Summary:	Qt-only wrapper for NetworkManager DBus API
Name:		libnm-qt
Version:	0.9.8
Release:	3.%{snapshot}.1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://projects.kde.org/projects/extragear/libs/libnm-qt
# Package from git snapshots, create example:
# git clone git://anongit.kde.org/libnm-qt.git
# cd libnm-qt
# git archive --prefix=libnm-qt-%{version}/ master | bzip2 > ../%{name}-%{version}-git%{git_commit}.tar.bz2
Source0:	%{name}-%{version}-git%{git_commit}.tar.bz2
BuildRequires:	cmake
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(ModemManagerQt)
BuildRequires:	pkgconfig(NetworkManager) >= 0.9.8
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)

%description
Qt library for NetworkManager.

%package -n %{libname}
Summary:	Qt-only wrapper for NetworkManager DBus API
Group:		System/Libraries

%description -n %{libname}
Qt library for NetworkManager.


%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Qt libraries and header files for developing applications
that use NetworkManager.

%prep
%setup -qn %{name}-%{version}-git%{git_commit}

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libNetworkManagerQt.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/NetworkManagerQt.pc
%{_libdir}/libNetworkManagerQt.so
%{_includedir}/NetworkManagerQt/
