#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Graph
Summary:	CGI::Graph - Create interactive CGI-based graphs
Summary(pl):	Modu³ CGI::Graph - tworz±cy interaktywne wykresy oparte na CGI
Name:		perl-CGI-Graph
Version:	0.93
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-CGI
BuildRequires:	perl-Data-Table
BuildRequires:	perl-GD
BuildRequires:	perl-GD-Graph
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module creates CGI graphs which allow the user to visualize
spreadsheet data using scatter plots, bar plots, histograms, etc. It
provides features for easy interactions such as panning, zooming,
element selection, and axis selection.

%description -l pl
Ten modu³ tworzy wykresy CGI, pozwalaj±ce na wizualizacjê danych z
arkuszy kalkulacyjncyh przy u¿yciu wykresów rozproszonych, s³upkowych,
histogramów itp. Daje mo¿liwo¶æ ³atwej interakcji takiej jak
przesuwanie, powiêkszanie, wybieranie elementów i osi.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
