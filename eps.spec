Summary:	Email Processing System
Summary(pl):	System przetwarzania e-maili
Name:		eps
Version:	1.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.inter7.com/eps/%{name}-%{version}.tar.gz
# Source0-md5:	20e2e7771e0d99138950ec85880a1d1a
Patch0:		%{name}-crlf.patch
URL:		http://www.inter7.com/eps.html
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EPS stands for Email Processing System. This package is intended to
give people the ability to write their own email processing tools.
Whether you want to process incoming and outgoing emails, or just
analyze a message, this package is intended to aid in that endeavor.

%description -l pl
EPS to system przetwarzania e-maili (Email Processing System - st±d
nazwa). Pakiet ma daæ ludziom mo¿liwo¶æ pisania w³asnych narzêdzi do
przetwarzania poczty elektronicznej. Je¶li chcemy przetwarzaæ listy
przychodz±ce lub wychodz±ce, albo tylko przeanalizowaæ wiadomo¶æ,
ten pakiet ma pomóc tych staraniach.

%package devel
Summary:	Header files for EPS library
Summary(pl):	Pliki nag³ówkowe biblioteki EPS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for EPS library.

%description devel -l pl
Pliki nag³ówkowe biblioteki EPS.

%package static
Summary:	Static EPS library
Summary(pl):	Statyczna biblioteka EPS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static EPS library.

%description static -l pl
Statyczna biblioteka EPS.

%prep
%setup -q
%patch -p1

%build
%{__make} libeps.a \
	CC="libtool --mode=compile %{__cc}" \
	DEFS="%{rpmcflags} -Wall -I."

libtool --mode=link %{__cc} -o libeps.la *.lo -rpath %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/eps

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
