Summary:	Email Processing System
Summary(pl.UTF-8):	System przetwarzania e-maili
Name:		eps
Version:	1.7
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://www.inter7.com/eps/%{name}-%{version}.tar.gz
# Source0-md5:	55385a89db651207c4f8a3c49bd1f8e6
URL:		http://www.inter7.com/?page=eps
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EPS stands for Email Processing System. This package is intended to
give people the ability to write their own email processing tools.
Whether you want to process incoming and outgoing emails, or just
analyze a message, this package is intended to aid in that endeavor.

%description -l pl.UTF-8
EPS to system przetwarzania e-maili (Email Processing System - stąd
nazwa). Pakiet ma dać ludziom możliwość pisania własnych narzędzi do
przetwarzania poczty elektronicznej. Jeśli chcemy przetwarzać listy
przychodzące lub wychodzące, albo tylko przeanalizować wiadomość,
ten pakiet ma pomóc w tych staraniach.

%package devel
Summary:	Header files for EPS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki EPS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for EPS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki EPS.

%package static
Summary:	Static EPS library
Summary(pl.UTF-8):	Statyczna biblioteka EPS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static EPS library.

%description static -l pl.UTF-8
Statyczna biblioteka EPS.

%prep
%setup -q

%build
%{__make} libeps.a \
	CC="libtool --mode=compile %{__cc}" \
	DEFS="%{rpmcppflags} %{rpmcflags} -Wall -I."

libtool --mode=link %{__cc} -o libeps.la *.lo -rpath %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

touch libeps.so

%{__make} install \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
	INCDIR=$RPM_BUILD_ROOT%{_includedir}/eps

libtool --mode=install install libeps.la $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO doc/{credits,howto,license}
%attr(755,root,root) %{_libdir}/libeps.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeps.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeps.so
%{_libdir}/libeps.la
%{_includedir}/eps

%files static
%defattr(644,root,root,755)
%{_libdir}/libeps.a
