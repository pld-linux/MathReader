Summary:	Mathematica Notebook Reader
Summary(pl):	Przegl±darka plików z programu Mathematica
Name:		MathReader
Version:	5.0.1
Release:	2
License:	almost free, distributable
Group:		Applications/Math
# from http://www.wolfram.com/products/mathreader/download.cgi
Source0:	%{name}_%{version}_Linux.sh
# Source0-md5:	35b7144eff51e017a03bf5c68d743548
Source1:	%{name}_%{version}_Linux-AMD64.sh
# Source1-md5:	54c0db30f9a78269c03c970aaa841b66
Source2:	%{name}_%{version}_Linux-AXP.sh
# Source2-md5:	9ab612c9543c69838dd38445dd0e8b05
Source3:	%{name}_%{version}_Linux-IA64.sh
# Source3-md5:	6ea3a14eac68391da213a25d62c629d4
# based on http://www.wolfram.com/products/mathreader/licenseagreement.html
Source4:	%{name}-license.txt
Source5:	%{name}.desktop
URL:		http://www.wolfram.com/products/mathreader/
BuildRequires:	rpmbuild(macros) >= 1.213
ExclusiveArch:	%{ix86} alpha %{x8664} ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MathReader is a viewer for notebook documents created with
Mathematica, the world's only fully integrated technical computing
system. MathReader lets you display and print Mathematica notebooks,
animate graphics, play sounds, and copy information from notebooks to
other documents. MathReader can be used by most web browsers as a
helper application for viewing notebook documents.

%description -l pl
MathReader jest przegl±dark± dla dokumentów utworzonych w programie
Mathematica, jedynym w ¶wiecie w pe³ni zintegrowanym systemie
technicznych obliczeñ. MathReader pozwala wy¶wietlaæ i drukowaæ
notatki, odtwarzaæ animacje, odgrywaæ d¼wiêki i kopiowaæ informacje z
notatek programu Mathematica do innych dokumentów. MathReader mo¿e byæ
te¿ u¿ywany przez wiêkszo¶æ przegl±darek WWW jako aplikacja pomocnicza
do przegl±dania dokumentów.

%prep

%install
rm -rf $RPM_BUILD_ROOT

%ifarch %{ix86}
%define _source	%{SOURCE0}
%endif
%ifarch %{x8664}
%define	_source	%{SOURCE1}
%endif
%ifarch alpha
%define	_source	%{SOURCE2}
%endif
#%%ifarch ia64
#%%define	_source	%{SOURCE3}
#%%endif

sh %{_source} auto \
	-targetdir=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	-execdir=$RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
ln -sf %{_libdir}/%{name}/Executables/{MathReader,mathreader} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE4} .
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-license.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/Executables
%{_libdir}/%{name}/Configuration
%{_libdir}/%{name}/Documentation
%dir %{_libdir}/%{name}/SystemFiles
%{_libdir}/%{name}/SystemFiles/CharacterEncodings
%dir %{_libdir}/%{name}/SystemFiles/FrontEnd
%dir %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries/Linux
%endif
%ifarch %{x8664}
%attr(755,root,root) %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries/Linux-x86-64
%endif
%ifarch alpha
%attr(755,root,root) %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries/Linux-AXP
%endif
%{_libdir}/%{name}/SystemFiles/FrontEnd/StyleSheets
%{_libdir}/%{name}/SystemFiles/FrontEnd/SystemResources
%{_libdir}/%{name}/SystemFiles/FrontEnd/TextResources
%{_libdir}/%{name}/SystemFiles/Fonts
%{_libdir}/%{name}/SystemFiles/Installation
%{_libdir}/%{name}/SystemFiles/SpellingDictionaries
%{_desktopdir}/%{name}.desktop
