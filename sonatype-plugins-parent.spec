%global pkg_name sonatype-plugins-parent
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global tag a594629

Name:           %{?scl_prefix}%{pkg_name}
Version:        8
Release:        6.12%{?dist}
Summary:        Sonatype Plugins Parent POM
BuildArch:      noarch
License:        ASL 2.0
URL:            https://github.com/sonatype/oss-parents
Source:         https://github.com/sonatype/oss-parents/tarball/plugins-parent-%{version}#/%{pkg_name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}forge-parent

%description
This package provides Sonatype plugins parent POM used by other Sonatype
packages.

%prep
%setup -q -n sonatype-oss-parents-%{tag}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cp -p %{SOURCE1} LICENSE
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cd ./plugins-parent
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
cd ./plugins-parent
%mvn_install
%{?scl:EOF}

%files -f plugins-parent/.mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE

%changelog
* Mon Feb 08 2016 Michal Srb <msrb@redhat.com> - 8-6.12
- Fix BR on maven-local & co.

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 8-6.11
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 8-6.10
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 8-6.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 8-6.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 8-6.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-6.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-6.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-6.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 8-6.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-6.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-6.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 8-6
- Mass rebuild 2013-12-27

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 8-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-3
- Build with xmvn

* Wed Dec 12 2012 Michal Srb <msrb@redhat.com> - 8-2
- Added license (Resolves: #884637)

* Wed Aug  8 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 8-1
- Initial packaging
