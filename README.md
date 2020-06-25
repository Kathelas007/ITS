# ITS - Testing and Dynamic Analysis

Part1 - Create test plan of e-commerce using Behave  
Part2 - Implement created scenarios using Selenium  

## Part 1
Dejme tomu, že pracujeme ve vývojovém týmu, jehož cílem je vytvořit internetový obchod s mimozemskými artefakty. Softwaroví architekti vybrali jedno z obecných řešení s otevřeným zdrojovým kódem, ale nejsou si jistí jeho kvalitou. Bylo rozhodnuto, že kvůli dalšímu procesu vývoje je potřeba mít automatizované testy ověřující základní funkcionalitu daného řešení. Byla vybrána technologie BDD a Selenium, i když s danými technologiemi nemá ve vývojovém týmu nikdo žádnou zkušenost. Vaším cílem je tento nedostatek eliminovat, navrhnout a implementovat testy pro daný internetový obchod.

### Cílem projektu je:
Podrobně se seznámit se zadanou oblastí testované aplikace (zdrojem nechť jsou dokumentace na internetu, selský rozum v případě neexistující dokumentace nebo informace od zadavatele projektu). Zvolit a navrhnout, co je cílem testů (které části povrchově do šířky nebo hloubkově do detailu budou testované).

Nastudovat chováním řízený vývoj (Behaviour-driven development, BDD).

Vypracovat scénáře BDD pro testování zadané oblasti testované aplikace. Podrobné pokyny jsou níže.

Na 1. projekt navazuje 2. projekt, ve kterém budete implementovat vámi navržené testy pomocí nástroje Selenium a Behave (Dokumentace). Toto je třeba zohlednit při tvorbě testovacích scénářů BDD. Na hodnocení prvního projektu bude mít největší vliv váš výběr testovaných částí a kvalita vypracování testovacích scénářů.

###  Testovaná aplikace

Testovanou aplikací je instance eCommerce platforma OpenCart.


### Instance a jejich správa
Každý student má přiřazenou jednu instanci. Seznam instancí se liší TCP portem, na které daná instance poslouchá.

Každý eCommerce systém má své administrativní rozhraní (login a heslo je "admin").

Reset instancí (návrat do původního stavu) je možný pomocí příslušného odkazu/tlačítka v seznamu instancí.

Jednotlivé instance jsou obecně přístupné - buďte prosím slušní a nezasahujte do cizích instancí.

### Testovací cíl
S danou aplikací se seznamte a vyberte si podčást, pro kterou navrhnete testovací plán. Mějte na mysli, že vámi navržené testovací scénáře budete později implementovat jako automatizované testy. Inspirace pro vybrané podčásti:

    Nákupní proces produktu.
    Správa produktů v administraci.
    Správa uživatelů.
    Správa objednávek.
    ...

### Pokyny k vypracování testovacích scénářů
Scénáře BDD vypracujte v souborech s příponou .feature. Syntaxi jazyka, význam příkazů a nejlepší praktiky pro psaní scénářů nastudujte dle dokumentace, doporučené četby a vlastních zdrojů. Minimální počet scénářů není definován, avšak bude mít vliv na hodnocení projektu. Zároveň ve volbě rozsahu scénářů zohledněte, že ve druhém projektu budete implementovat odpovídající testovací případy pomocí automatizovaných testů GUI. Testování GUI bude tématem dalších přednášek.

Soubory se scénáři musí doprovázet soubor README.md, který bude obsahovat stručný popis testovaných vlastností.

Cílem souboru je seznámit čtenáře s rozsahem testovaných vlastností a vztahem těchto vlastností k jednotlivým souborům popisující scénáře BDD.

Obsah souboru není definován, kladně hodnocené budou přehledné, stručné a zároveň úplné popisy.

Soubor README.md bude ve formátu Markdown. Používejte co nejméně formátování, ideálně tedy variantu strict. Ověřit validitu textu ve formátu Markdown můžete na konvertoru pandoc. Jazyk textu může být CZ/SK/EN, vše UTF-8.

## Part 2

### Cíl

Vytvořte automatické testy (Selenium) pro vámi navrženou testovací sadu na 
základě BDD scénářů.

### Úkoly

1. Nastudujte integrované prostředí pro tvorbu testů Selenium IDE:

    [ITS10] Přednáška ITS v 9. týdnu LS 2019/20
    [SeleniumIDE] http://www.seleniumhq.org/projects/ide/
    [SeleniumPythonBindings] http://selenium-python.readthedocs.io/

1.1 Nainstalujte si Selenium IDE pro Chrome nebo Firefox.

    Potřebujete prohlížeč s nainstalovaným rozšířením Selenium IDE. Na stránce
    http://www.seleniumhq.org/download/ hledejte "Selenium IDE". V době psaní
    zadání byla aktuální verze 3.17 (rozšíření pro Chrome).

1.2 Vytvořte si zkušební test principem nahrání (record+replay) v Selenium IDE.

    Zajímavé odkazy pro verze Selenium IDE <3.0:

    [SeleniumDocs] https://www.selenium.dev/documentation/en/
    [SeleniumYoutube]
    https://www.youtube.com/results?search_query=selenium+ide

    Někdy pro identifikaci objektů/cílů pro příkazy Selenia nestačí
    identifikace poskytnutá skrz Selenium IDE (name, id, link text), ale je
    potřeba identifikaci upřesnit. K tomu může posloužit CSS selektor nebo
    výraz XPath.

    [CSSSelectors] http://www.w3schools.com/cssref/css_selectors.asp
    [ChromeConsoleXPath] https://stackoverflow.com/a/22573161
    [XPath] http://www.w3schools.com/xpath/

1.3 Nainstalujte si projekt behave [Behave] pro automatizaci BDD testů. Vyzkoušejte
    si základní příklad [BDDHello].

    [Behave] https://behave.readthedocs.io/en/latest/install.html
    [BDDHello] https://behave.readthedocs.io/en/latest/tutorial.html

1.4 Nainstalujte si rozhraní Selenium pro jazyk Python3 (modul selenium). V tomto
    projektu se očekává Python verze 3.

    [PyPi] https://pypi.python.org/pypi/selenium
    [RTDInstall] https://selenium-python.readthedocs.org/installation.html

    V případě, že nemáte počítač s administrátorským přístupem:
    [PipUser] https://pip.pypa.io/en/latest/user_guide.html#user-installs

1.5 Upravte test v jazyce Python pro spuštění na Selenium Server.

    Používejte selenium.webdriver.Remote. Inspirujte se na [RTDSeServer] a
    příkladem [WDMys]. Selenium server/grid pro účely projektu ITS je
    na [ITSSS]. Spouštěč testů (WebDriver, DesiredCapabilities) může být buď
    FIREFOX i CHROME (k dispozici jsou oba).

    Časový limit pro čekání na DOM elementy je doporučen max 15 sekund.

    [ITSSS] http://mys01.fit.vutbr.cz:4444/wd/hub
    [RTDSeServer]
    https://selenium-python.readthedocs.org/getting-started.html#using-selenium-with-remote-webdriver
    [WDMys] https://www.fit.vutbr.cz/study/courses/ITS/private/mys01.py

2. Implementujte automatizované testy vaší sekce testované aplikace.

2.1 Testy budou zahrnovat vámi navržené testy v testovacím plánu odevzdaným
    v prvním projektu. Implementované testy nemusí byt úplně stejné, jako testy
    popsané v návrhu testů v testovacím plánu.

    Zajímavé odkazy:
    [SeleniumPractices]
    https://mestachs.wordpress.com/2012/08/13/selenium-best-practices/
    [PageObject]
    http://blog.activelylazy.co.uk/2011/07/09/page-objects-in-selenium-2-0/
    [PageObjectEx]
    https://weblogs.java.net/blog/johnsmart/archive/2010/08/09/selenium-2web-driver-land-where-page-objects-are-king

2.2 Testy ověřte na (a přizpůsobte ke) spuštění na vzdáleném Selenium Server.

    Daný selenium server [ITSSS] je připraven pro hodnocení projektů.
    Připravte proto testy pro toto běhové prostředí.

3. Sepište report (volitené).

   Report není povinný. Report sepište, pokud:
     * jste našli nějakou chybu (report musí obsahovat popis chyby), nebo
     * pokud se implementované testy liší od navržených testů v 1. projektu.
   V jiném případě report nepište.

3.1 Požadavky na report:

  Formát reportu je PDF, rozsah 1-3 strany. Report obsahuje následující části:

  1. hlavičku,
  2. testy v původním plánu neimplementované,
  3. testy implementované a nepopsané v původním plánu,
  3.1 popis nových testů.
  4. nalezené chyby v podobě stručného hlášení o chybách (bug report).

  Pokud by nějaká část měla být prázdná, do reportu ji nezahrnujte.

4. Odevzdejte své řešení prostřednictvím archivu xLOGIN99.zip. Archiv bude
   obsahovat:

    -/                  kořenový adresář archivu
     +- report.pdf      (nepovinný) report z testování
     +- features/
        +- *.feature    soubory se scénáři
        +- steps/
           +- *.py      soubory s kroky Python-Selenium


   Pro spuštění testů ! na Selenium Serveru [ITSSS] ! musí být úspěšně
   provedeny tyto kroky:

   $ unzip xLOGIN99.zip
   $ [ -f requirements.txt ] && pip3 install -r requirements.txt
   $ behave

