grammar Grammar;

program: (statement NEWLINE)* EOF;



statement: assing | print | if_statement | for_statement;
//Definimos la asignacion/
//assing: ID'='expr;


//2.- DEFINIMOS LA ASIGNACION CON TIPO */
assing:type ID '='expr;
//DEFINIMOS LOS TIPOS
type: 'int' | 'string';


//Definimos print/
print:'print''('expr')';

//Definimos if/
if_statement: 'if''('expr')'block;

//Definimos for/
for_statement:'for''('assing';'expr';'assing')'block;

//Definimos block/
block:'{'(statement NEWLINE)*'}';

//Definimos expr/
expr: expr op=('*'|'/')expr
    | expr op=('+'|'-')expr
    | expr op=('>'|'<'|'>='|'<=')expr
    | expr op=('=='|'!=')expr
    |ID 
    
//DEFINICION DE VALORES NUMERICOS
    |NUMBER
//AGREGAMOS STRING ALA EXPRESIONI
    |STRING
    |'('expr')'
    ;




//Deficion de elementos finales/
ID:[a-zA-Z][a-zA-Z_0-9]*;


//agregamos reglas para los numeros 
NUMBER:[0-9]+;

//AGREGAMOS REGLAS PARA STRIING
STRING: '"' (~["\r\n])*?'"';


NEWLINE:[\r\n];
WS:[\t]->skip;
SEMI:';';