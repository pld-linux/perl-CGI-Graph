#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Graph
Summary:	CGI::Graph - create interactive CGI-based graphs
Summary(pl):	CGI::Graph - tworzenie interaktywnych wykresów w oparciu o CGI
Name:		perl-CGI-Graph
Version:	0.93
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}%{pnam}-%{version}.tar.gz
# Source0-md5:	e18432d8462620a390ac8f686977ad43
BuildRequires:	perl-devel >= 5.6
%if %{with tests}
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
Ten modu³ tworzy wykresy CGI, pozwalaj±ce na wizualizacjê danych z
arkuszy kalkulacyjncyh przy u¿yciu wykresów rozproszonych, s³upkowych,
histogramów itp. Daje mo¿liwo¶æ ³atwej interakcji takiej jak
przesuwanie, powiêkszanie, wybieranie elementów i osi.

%prep
%setup -q -n %{pdir}%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
