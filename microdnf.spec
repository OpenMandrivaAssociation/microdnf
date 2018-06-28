Summary:	Minimal C implementation of DNF
Name:		microdnf
Version:	3.0.1
Release:	1
License:	GPLv2+
Group:		Development/Other
URL:		https://github.com/rpm-software-management/microdnf/
Source0:	%{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	meson
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(libpeas-1.0)
BuildRequires:	pkgconfig(libdnf)
BuildRequires:	pkgconfig(smartcols)
BuildRequires:	pkgconfig(libsolv)

%description
A minimal DNF for (mostly) Docker containers that
uses libhif and hence doesn't require Python.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_instal

%files
%{_bindir}/%{name}
