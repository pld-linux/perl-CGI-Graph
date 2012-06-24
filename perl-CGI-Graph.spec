#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Graph
Summary:	CGI::Graph - Create interactive CGI-based graphs
Summary(pl):	Modu� CGI::Graph - tworz�cy interaktywne wykresy oparte na CGI
Name:		perl-CGI-Graph
Version:	0.93
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	e18432d8462620a390ac8f686977ad43
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-CGI
BuildRequires:	perl-Data-Table
BuildRequires:	perl-GD
BuildRequires:	perl-GD-Graph
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module creates CGI graphs which allow the user to visualize
spreadsheet data using scatter plots, bar plots, histograms, etc. It
provides features for easy interactions such as panning, zooming,
element selection, and axis selection.

%description -l pl
Ten modu� tworzy wykresy CGI, pozwalaj�ce na wizualizacj� danych z
arkuszy kalkulacyjncyh przy u�yciu wykres�w rozproszonych, s�upkowych,
histogram�w itp. Daje mo�liwo�� �atwej interakcji takiej jak
przesuwanie, powi�kszanie, wybieranie element�w i osi.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
