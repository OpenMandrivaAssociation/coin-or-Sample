%global		module		Sample

Name:		coin-or-%{module}
Group:		Sciences/Mathematics
Summary:	Coin-or Sample data files
Version:	1.2.3
Release:	1
License:	Public Domain
URL:		https://projects.coin-or.org/svn/Data/%{module}
Source0:	http://www.coin-or.org/download/source/Data/%{module}-%{version}.tgz
Source1:	COPYING
BuildArch:	noarch

%description
Coin-or Sample data files.

%prep
%setup -q -n %{module}-%{version}

%build
%configure
cp -p %{SOURCE1} .
make %{?_smpflags} all

%install
make install DESTDIR=%{buildroot} pkgconfiglibdir=%{_datadir}/pkgconfig

%files
%{_datadir}/coin
%{_datadir}/pkgconfig/*
%doc COPYING
