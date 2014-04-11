%global		module		Sample

Name:		coin-or-%{module}

Summary:	Coin-or Sample data files
Version:	1.2.8
Release:	1%{?dist}
License:	Public Domain
URL:		https://projects.coin-or.org/svn/Data/%{module}
Source0:	http://www.coin-or.org/download/source/Data/%{module}-%{version}.tgz
Source1:	COPYING
Source2:	%{name}.rpmlintrc
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

%changelog
* Fri Nov  1 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.8-1
- Update to latest upstream release.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.3-4
- Preserve timestamp of COPYING (#894610#c10)

* Tue Jan 15 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.3-3
- Add a more descriptive summary (#894610#c8)
- Install pkgconfig files to noarch directory (#894610#c8)
- Install a COPYING file to justify Public Domain license (#894610#c8)

* Mon Jan 14 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.3-2
- Update license (#894610#c4).

* Fri Nov 23 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2.3-1
- Initial coinor-Sample spec.
