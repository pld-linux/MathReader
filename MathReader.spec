# TODO:
# - version for PPC/alpha/IA64/AMD64
# - talk with wolfram about redistribute it ;)
Summary:	Mathematica Notebook Reader
Summary(pl):	Przegl±darka plików z programu Mathematica
Name:		MathReader
Version:	5.0.1
Release:	1
License:	Almost Free... look at http://www.wolfram.com/products/mathreader/licenseagreement.html
# from http://www.wolfram.com/products/mathreader/download.cgi
Source0:	%{name}_%{version}_Linux.sh
Group:		Applications/Math
URL:		http://www.wolfram.com/products/mathreader/
ExclusiveArch:	%{ix86}
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

sh %{SOURCE0} auto \
	-targetdir=$RPM_BUILD_ROOT%{_libdir}/%{name} \
	-execdir=$RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_libdir}/%{name}/Executables/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/SystemFiles/FrontEnd/Binaries/Linux
%attr(755,root,root) %{_libdir}/%{name}/Executables
%attr(755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}/SystemFiles/SpellingDictionaries
%{_libdir}/%{name}/SystemFiles/Installation
%{_libdir}/%{name}/SystemFiles/FrontEnd/TextResources
%{_libdir}/%{name}/SystemFiles/FrontEnd/SystemResources
%{_libdir}/%{name}/SystemFiles/FrontEnd/StyleSheets
%{_libdir}/%{name}/SystemFiles/Fonts
%{_libdir}/%{name}/SystemFiles/CharacterEncodings
%{_libdir}/%{name}/Documentation
%{_libdir}/%{name}/Configuration
