%define upstream_name    XML-Parser-Style-EasyTree
Name:		perl-%{upstream_name}
Version:	0.09
Release:	7

Summary:	Parse xml to simple tree
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-Parser-Style-EasyTree
Source0:	https://cpan.metacpan.org/authors/id/M/MO/MONS/XML-Parser-Style-EasyTree-%{version}.tar.gz
Patch0:		XML-Parser-Style-EasyTree-0.09-fix-version-for-cpanplus.patch

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ex::lib)
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

Requires:	perl(ex::lib)

%description
Parse xml to simple tree.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch0 -p0 -b .cpanplus

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 655611
- add br
- fix path applying
- rebuild for updated spec-helper

* Thu Dec 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 484438
- make version parsable by cpanplus

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 421828
- update to 0.09

* Thu Aug 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 421622
- update to 0.08

* Mon Aug 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 420268
- update to 0.05

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 401464
- rebuild
- using %0.09 fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.03-2mdv2010.0
+ Revision: 375886
- rebuild

* Mon Mar 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.1
+ Revision: 355663
- update to new version 0.03

* Sun Mar 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.02-1mdv2009.1
+ Revision: 355232
- adding missing requires
- import perl-XML-Parser-Style-EasyTree


* Fri Feb 20 2009 cpan2dist 0.02-1mdv
- initial mdv release, generated with cpan2dist

