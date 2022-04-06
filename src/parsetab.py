
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEPERCENTrightUMINUSAND COMMA DIVIDE DO DOUBLE DOUBLE_CONST ECHO ELSE ENDIF ENDSUBROUTINE ENDWHILE EQUALITY EQUALS FLOORDIV FOR GREATER_EQUAL GREATER_THAN IF INPUT INT INT_CONST LBRACKET LESS_EQUAL LESS_THAN LPAREN MINUS MOD NEWLINE NEXT NOT NOT_EQUALITY OR OUTPUT PERCENT PLUS PRINT RBRACKET RETURN RPAREN STRING_CONST SUBROUTINE THEN TIMES TO VAR WHILEstatement : stmt_liststmt_list : simple_stmt\n                     | stmt_list NEWLINE simple_stmtif_stmt : IF expression THEN NEWLINE stmt_list NEWLINE ENDIF\n                   | IF expression THEN NEWLINE stmt_list NEWLINE ELSE NEWLINE stmt_list NEWLINE ENDIF\n                   | IF expression THEN NEWLINE stmt_list NEWLINE ELSE if_stmtwhile_stmt : WHILE expression DO NEWLINE stmt_list NEWLINE ENDWHILEfor_stmt : FOR assignment_stmt TO expression NEWLINE stmt_list NEWLINE NEXT VARsimple_stmt : expression\n                       | expr_list\n                       | arg_list\n                       | assignment_stmt\n                       | array_decl_stmt\n                       | if_stmt\n                       | while_stmt\n                       | for_stmt\n                       | output_stmt\n                       | input_stmt\n                       | function_stmt\n                       | return_stmtarray_decl_stmt : DOUBLE array_index\n                           | INT array_indexassignment_stmt : VAR EQUALS expressionassignment_stmt : array_index EQUALS expressioninput_stmt : INPUT VAR\n                      | INPUT array_indexoutput_stmt : OUTPUT expressionreturn_stmt : RETURN expressionfunction_header : INT SUBROUTINE VAR LPAREN arg_list RPAREN\n                           | DOUBLE SUBROUTINE VAR LPAREN arg_list RPAREN\n                           | INT SUBROUTINE VAR LPAREN RPAREN\n                           | DOUBLE SUBROUTINE VAR LPAREN RPARENfunction_stmt : function_header NEWLINE stmt_list NEWLINE ENDSUBROUTINEarg_list : INT VAR\n                    | DOUBLE VAR\n                    | arg_list COMMA INT VAR\n                    | arg_list COMMA DOUBLE VARexpr_list : expression COMMA expression\n                     | expr_list COMMA expressionexpression : expression PLUS expression\n                      | expression MINUS expression\n                      | expression TIMES expression\n                      | expression DIVIDE expression\n                      | expression PERCENT expression\n                      | expression FLOORDIV expression\n                      | expression MOD expression expression : expression LESS_THAN expression\n                      | expression GREATER_THAN expression\n                      | expression LESS_EQUAL expression\n                      | expression GREATER_EQUAL expression\n                      | expression EQUALITY expression\n                      | expression NOT_EQUALITY expression expression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : VAR LPAREN expression RPAREN\n                      | VAR LPAREN expr_list RPAREN\n                      | VAR LPAREN RPARENexpression : array_indexarray_index : VAR LBRACKET expression RBRACKETexpression : literalliteral : INT_CONSTliteral : DOUBLE_CONSTliteral : STRING_CONSTexpression : VAR'
    
_lr_action_items = {'MINUS':([0,4,16,17,18,19,20,23,24,26,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,57,64,65,69,72,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,103,107,108,109,112,113,114,115,124,130,131,136,137,142,],[16,35,16,16,-64,-58,-60,16,16,16,16,-61,-62,-63,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-53,-64,-58,35,16,16,16,16,35,35,35,16,35,-40,-41,-42,-43,-44,35,35,35,35,35,35,35,35,35,35,-54,35,-57,35,35,35,16,-55,-56,-59,16,16,35,16,16,16,16,16,16,16,]),'LPAREN':([0,16,17,18,23,24,26,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,54,55,56,57,72,99,100,103,112,113,115,124,130,131,136,137,142,],[17,17,17,54,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,54,17,17,17,17,17,110,111,17,17,17,17,17,17,17,17,17,17,]),'VAR':([0,16,17,21,22,23,24,25,26,27,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,60,63,72,90,91,103,112,113,115,116,119,124,130,131,136,137,139,142,],[18,51,51,58,61,51,51,67,51,70,51,18,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,99,100,18,105,106,51,18,18,18,126,128,18,18,18,18,18,141,18,]),'INT':([0,33,49,72,110,111,112,113,115,124,130,131,136,137,142,],[21,21,90,21,116,116,21,21,21,21,21,21,21,21,21,]),'DOUBLE':([0,33,49,72,110,111,112,113,115,124,130,131,136,137,142,],[22,22,91,22,119,119,22,22,22,22,22,22,22,22,22,]),'IF':([0,33,72,112,113,115,124,130,131,134,136,137,142,],[23,23,23,23,23,23,23,23,23,23,23,23,23,]),'WHILE':([0,33,72,112,113,115,124,130,131,136,137,142,],[24,24,24,24,24,24,24,24,24,24,24,24,]),'FOR':([0,33,72,112,113,115,124,130,131,136,137,142,],[25,25,25,25,25,25,25,25,25,25,25,25,]),'OUTPUT':([0,33,72,112,113,115,124,130,131,136,137,142,],[26,26,26,26,26,26,26,26,26,26,26,26,]),'INPUT':([0,33,72,112,113,115,124,130,131,136,137,142,],[27,27,27,27,27,27,27,27,27,27,27,27,]),'RETURN':([0,33,72,112,113,115,124,130,131,136,137,142,],[29,29,29,29,29,29,29,29,29,29,29,29,]),'INT_CONST':([0,16,17,23,24,26,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,72,103,112,113,115,124,130,131,136,137,142,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'DOUBLE_CONST':([0,16,17,23,24,26,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,72,103,112,113,115,124,130,131,136,137,142,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'STRING_CONST':([0,16,17,23,24,26,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,72,103,112,113,115,124,130,131,136,137,142,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20,30,31,32,50,51,52,58,59,61,62,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,94,96,98,105,106,107,108,109,125,133,135,138,141,143,],[0,-1,-2,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-64,-58,-60,-61,-62,-63,-53,-64,-58,-34,-22,-35,-21,-27,-25,-26,-28,-3,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-38,-39,-54,-57,-23,-24,-36,-37,-55,-56,-59,-33,-4,-7,-6,-8,-5,]),'NEWLINE':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20,28,30,31,32,50,51,52,58,59,61,62,69,70,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,94,96,98,101,102,104,105,106,107,108,109,114,118,121,122,123,125,127,129,132,133,134,135,138,140,141,143,],[33,-2,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-64,-58,-60,72,-61,-62,-63,-53,-64,-58,-34,-22,-35,-21,-27,-25,-26,-28,-3,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-38,-39,-54,-57,-23,-24,112,113,115,-36,-37,-55,-56,-59,124,-31,-32,130,131,-33,-29,-30,136,-4,137,-7,-6,142,-8,-5,]),'PLUS':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[34,-64,-58,-60,-61,-62,-63,-53,-64,-58,34,34,34,34,34,-40,-41,-42,-43,-44,34,34,34,34,34,34,34,34,34,34,-54,34,-57,34,34,34,-55,-56,-59,34,]),'TIMES':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[36,-64,-58,-60,-61,-62,-63,-53,-64,-58,36,36,36,36,36,36,36,-42,-43,-44,36,36,36,36,36,36,36,36,36,36,-54,36,-57,36,36,36,-55,-56,-59,36,]),'DIVIDE':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[37,-64,-58,-60,-61,-62,-63,-53,-64,-58,37,37,37,37,37,37,37,-42,-43,-44,37,37,37,37,37,37,37,37,37,37,-54,37,-57,37,37,37,-55,-56,-59,37,]),'PERCENT':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[38,-64,-58,-60,-61,-62,-63,-53,-64,-58,38,38,38,38,38,38,38,-42,-43,-44,38,38,38,38,38,38,38,38,38,38,-54,38,-57,38,38,38,-55,-56,-59,38,]),'FLOORDIV':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[39,-64,-58,-60,-61,-62,-63,-53,-64,-58,39,39,39,39,39,-40,-41,-42,-43,-44,39,39,39,39,39,39,39,39,39,39,-54,39,-57,39,39,39,-55,-56,-59,39,]),'MOD':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[40,-64,-58,-60,-61,-62,-63,-53,-64,-58,40,40,40,40,40,-40,-41,-42,-43,-44,40,40,40,40,40,40,40,40,40,40,-54,40,-57,40,40,40,-55,-56,-59,40,]),'LESS_THAN':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[41,-64,-58,-60,-61,-62,-63,-53,-64,-58,41,41,41,41,41,-40,-41,-42,-43,-44,41,41,41,41,41,41,41,41,41,41,-54,41,-57,41,41,41,-55,-56,-59,41,]),'GREATER_THAN':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[42,-64,-58,-60,-61,-62,-63,-53,-64,-58,42,42,42,42,42,-40,-41,-42,-43,-44,42,42,42,42,42,42,42,42,42,42,-54,42,-57,42,42,42,-55,-56,-59,42,]),'LESS_EQUAL':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[43,-64,-58,-60,-61,-62,-63,-53,-64,-58,43,43,43,43,43,-40,-41,-42,-43,-44,43,43,43,43,43,43,43,43,43,43,-54,43,-57,43,43,43,-55,-56,-59,43,]),'GREATER_EQUAL':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[44,-64,-58,-60,-61,-62,-63,-53,-64,-58,44,44,44,44,44,-40,-41,-42,-43,-44,44,44,44,44,44,44,44,44,44,44,-54,44,-57,44,44,44,-55,-56,-59,44,]),'EQUALITY':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[45,-64,-58,-60,-61,-62,-63,-53,-64,-58,45,45,45,45,45,-40,-41,-42,-43,-44,45,45,45,45,45,45,45,45,45,45,-54,45,-57,45,45,45,-55,-56,-59,45,]),'NOT_EQUALITY':([4,18,19,20,30,31,32,50,51,52,53,64,65,69,73,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,96,97,98,107,108,109,114,],[46,-64,-58,-60,-61,-62,-63,-53,-64,-58,46,46,46,46,46,-40,-41,-42,-43,-44,46,46,46,46,46,46,46,46,46,46,-54,46,-57,46,46,46,-55,-56,-59,46,]),'COMMA':([4,5,6,18,19,20,30,31,32,50,51,52,58,61,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,95,105,106,107,108,109,117,120,126,128,],[47,48,49,-64,-58,-60,-61,-62,-63,-53,-64,-58,-34,-35,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-38,-39,-54,47,-57,48,-36,-37,-55,-56,-59,49,49,-34,-35,]),'EQUALS':([18,19,67,68,109,],[55,57,55,57,-59,]),'LBRACKET':([18,51,58,61,67,70,],[56,56,56,56,56,56,]),'RPAREN':([20,30,31,32,50,51,52,53,54,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,93,94,95,105,106,107,108,109,110,111,117,120,126,128,],[-60,-61,-62,-63,-53,-64,-58,92,94,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-38,-39,-54,107,-57,108,-36,-37,-55,-56,-59,118,121,127,129,-34,-35,]),'THEN':([20,30,31,32,50,51,52,64,75,76,77,78,79,80,81,82,83,84,85,86,87,92,94,107,108,109,],[-60,-61,-62,-63,-53,-64,-58,101,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-54,-57,-55,-56,-59,]),'DO':([20,30,31,32,50,51,52,65,75,76,77,78,79,80,81,82,83,84,85,86,87,92,94,107,108,109,],[-60,-61,-62,-63,-53,-64,-58,102,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-54,-57,-55,-56,-59,]),'TO':([20,30,31,32,50,51,52,66,75,76,77,78,79,80,81,82,83,84,85,86,87,92,94,96,98,107,108,109,],[-60,-61,-62,-63,-53,-64,-58,103,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-54,-57,-23,-24,-55,-56,-59,]),'RBRACKET':([20,30,31,32,50,51,52,75,76,77,78,79,80,81,82,83,84,85,86,87,92,94,97,107,108,109,],[-60,-61,-62,-63,-53,-64,-58,-40,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-54,-57,109,-55,-56,-59,]),'SUBROUTINE':([21,22,],[60,63,]),'ENDSUBROUTINE':([115,],[125,]),'ENDIF':([130,142,],[133,143,]),'ELSE':([130,],[134,]),'ENDWHILE':([131,],[135,]),'NEXT':([136,],[139,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'stmt_list':([0,72,112,113,124,137,],[2,104,122,123,132,140,]),'simple_stmt':([0,33,72,112,113,115,124,130,131,136,137,142,],[3,74,3,3,3,74,3,74,74,74,3,74,]),'expression':([0,16,17,23,24,26,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,72,103,112,113,115,124,130,131,136,137,142,],[4,50,53,64,65,69,73,4,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,96,97,98,4,114,4,4,4,4,4,4,4,4,4,]),'expr_list':([0,33,54,72,112,113,115,124,130,131,136,137,142,],[5,5,95,5,5,5,5,5,5,5,5,5,5,]),'arg_list':([0,33,72,110,111,112,113,115,124,130,131,136,137,142,],[6,6,6,117,120,6,6,6,6,6,6,6,6,6,]),'assignment_stmt':([0,25,33,72,112,113,115,124,130,131,136,137,142,],[7,66,7,7,7,7,7,7,7,7,7,7,7,]),'array_decl_stmt':([0,33,72,112,113,115,124,130,131,136,137,142,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'if_stmt':([0,33,72,112,113,115,124,130,131,134,136,137,142,],[9,9,9,9,9,9,9,9,9,138,9,9,9,]),'while_stmt':([0,33,72,112,113,115,124,130,131,136,137,142,],[10,10,10,10,10,10,10,10,10,10,10,10,]),'for_stmt':([0,33,72,112,113,115,124,130,131,136,137,142,],[11,11,11,11,11,11,11,11,11,11,11,11,]),'output_stmt':([0,33,72,112,113,115,124,130,131,136,137,142,],[12,12,12,12,12,12,12,12,12,12,12,12,]),'input_stmt':([0,33,72,112,113,115,124,130,131,136,137,142,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'function_stmt':([0,33,72,112,113,115,124,130,131,136,137,142,],[14,14,14,14,14,14,14,14,14,14,14,14,]),'return_stmt':([0,33,72,112,113,115,124,130,131,136,137,142,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'array_index':([0,16,17,21,22,23,24,25,26,27,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,72,103,112,113,115,124,130,131,136,137,142,],[19,52,52,59,62,52,52,68,52,71,52,19,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,19,52,19,19,19,19,19,19,19,19,19,]),'literal':([0,16,17,23,24,26,29,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,72,103,112,113,115,124,130,131,136,137,142,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'function_header':([0,33,72,112,113,115,124,130,131,136,137,142,],[28,28,28,28,28,28,28,28,28,28,28,28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> stmt_list','statement',1,'p_statement','lz_parser.py',56),
  ('stmt_list -> simple_stmt','stmt_list',1,'p_stmt_list','lz_parser.py',61),
  ('stmt_list -> stmt_list NEWLINE simple_stmt','stmt_list',3,'p_stmt_list','lz_parser.py',62),
  ('if_stmt -> IF expression THEN NEWLINE stmt_list NEWLINE ENDIF','if_stmt',7,'p_if_stmt','lz_parser.py',71),
  ('if_stmt -> IF expression THEN NEWLINE stmt_list NEWLINE ELSE NEWLINE stmt_list NEWLINE ENDIF','if_stmt',11,'p_if_stmt','lz_parser.py',72),
  ('if_stmt -> IF expression THEN NEWLINE stmt_list NEWLINE ELSE if_stmt','if_stmt',8,'p_if_stmt','lz_parser.py',73),
  ('while_stmt -> WHILE expression DO NEWLINE stmt_list NEWLINE ENDWHILE','while_stmt',7,'p_while_stmt','lz_parser.py',85),
  ('for_stmt -> FOR assignment_stmt TO expression NEWLINE stmt_list NEWLINE NEXT VAR','for_stmt',9,'p_for_stmt','lz_parser.py',90),
  ('simple_stmt -> expression','simple_stmt',1,'p_simple_stmt','lz_parser.py',95),
  ('simple_stmt -> expr_list','simple_stmt',1,'p_simple_stmt','lz_parser.py',96),
  ('simple_stmt -> arg_list','simple_stmt',1,'p_simple_stmt','lz_parser.py',97),
  ('simple_stmt -> assignment_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',98),
  ('simple_stmt -> array_decl_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',99),
  ('simple_stmt -> if_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',100),
  ('simple_stmt -> while_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',101),
  ('simple_stmt -> for_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',102),
  ('simple_stmt -> output_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',103),
  ('simple_stmt -> input_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',104),
  ('simple_stmt -> function_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',105),
  ('simple_stmt -> return_stmt','simple_stmt',1,'p_simple_stmt','lz_parser.py',106),
  ('array_decl_stmt -> DOUBLE array_index','array_decl_stmt',2,'p_array_decl_stmt','lz_parser.py',111),
  ('array_decl_stmt -> INT array_index','array_decl_stmt',2,'p_array_decl_stmt','lz_parser.py',112),
  ('assignment_stmt -> VAR EQUALS expression','assignment_stmt',3,'p_assignment_stmt','lz_parser.py',127),
  ('assignment_stmt -> array_index EQUALS expression','assignment_stmt',3,'p_array_assign_stmt','lz_parser.py',140),
  ('input_stmt -> INPUT VAR','input_stmt',2,'p_input_stmt','lz_parser.py',149),
  ('input_stmt -> INPUT array_index','input_stmt',2,'p_input_stmt','lz_parser.py',150),
  ('output_stmt -> OUTPUT expression','output_stmt',2,'p_output_stmt','lz_parser.py',169),
  ('return_stmt -> RETURN expression','return_stmt',2,'p_return_stmt','lz_parser.py',174),
  ('function_header -> INT SUBROUTINE VAR LPAREN arg_list RPAREN','function_header',6,'p_function_header','lz_parser.py',179),
  ('function_header -> DOUBLE SUBROUTINE VAR LPAREN arg_list RPAREN','function_header',6,'p_function_header','lz_parser.py',180),
  ('function_header -> INT SUBROUTINE VAR LPAREN RPAREN','function_header',5,'p_function_header','lz_parser.py',181),
  ('function_header -> DOUBLE SUBROUTINE VAR LPAREN RPAREN','function_header',5,'p_function_header','lz_parser.py',182),
  ('function_stmt -> function_header NEWLINE stmt_list NEWLINE ENDSUBROUTINE','function_stmt',5,'p_function_stmt','lz_parser.py',210),
  ('arg_list -> INT VAR','arg_list',2,'p_arg_list','lz_parser.py',219),
  ('arg_list -> DOUBLE VAR','arg_list',2,'p_arg_list','lz_parser.py',220),
  ('arg_list -> arg_list COMMA INT VAR','arg_list',4,'p_arg_list','lz_parser.py',221),
  ('arg_list -> arg_list COMMA DOUBLE VAR','arg_list',4,'p_arg_list','lz_parser.py',222),
  ('expr_list -> expression COMMA expression','expr_list',3,'p_expr_list','lz_parser.py',239),
  ('expr_list -> expr_list COMMA expression','expr_list',3,'p_expr_list','lz_parser.py',240),
  ('expression -> expression PLUS expression','expression',3,'p_expression_arithmetic_binop','lz_parser.py',249),
  ('expression -> expression MINUS expression','expression',3,'p_expression_arithmetic_binop','lz_parser.py',250),
  ('expression -> expression TIMES expression','expression',3,'p_expression_arithmetic_binop','lz_parser.py',251),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_arithmetic_binop','lz_parser.py',252),
  ('expression -> expression PERCENT expression','expression',3,'p_expression_arithmetic_binop','lz_parser.py',253),
  ('expression -> expression FLOORDIV expression','expression',3,'p_expression_arithmetic_binop','lz_parser.py',254),
  ('expression -> expression MOD expression','expression',3,'p_expression_arithmetic_binop','lz_parser.py',255),
  ('expression -> expression LESS_THAN expression','expression',3,'p_expression_comp_binop','lz_parser.py',297),
  ('expression -> expression GREATER_THAN expression','expression',3,'p_expression_comp_binop','lz_parser.py',298),
  ('expression -> expression LESS_EQUAL expression','expression',3,'p_expression_comp_binop','lz_parser.py',299),
  ('expression -> expression GREATER_EQUAL expression','expression',3,'p_expression_comp_binop','lz_parser.py',300),
  ('expression -> expression EQUALITY expression','expression',3,'p_expression_comp_binop','lz_parser.py',301),
  ('expression -> expression NOT_EQUALITY expression','expression',3,'p_expression_comp_binop','lz_parser.py',302),
  ('expression -> MINUS expression','expression',2,'p_expression_unop','lz_parser.py',324),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','lz_parser.py',329),
  ('expression -> VAR LPAREN expression RPAREN','expression',4,'p_expression_func_call','lz_parser.py',334),
  ('expression -> VAR LPAREN expr_list RPAREN','expression',4,'p_expression_func_call','lz_parser.py',335),
  ('expression -> VAR LPAREN RPAREN','expression',3,'p_expression_func_call','lz_parser.py',336),
  ('expression -> array_index','expression',1,'p_expression_array_expr','lz_parser.py',354),
  ('array_index -> VAR LBRACKET expression RBRACKET','array_index',4,'p_expression_array_val','lz_parser.py',359),
  ('expression -> literal','expression',1,'p_expression_literal','lz_parser.py',367),
  ('literal -> INT_CONST','literal',1,'p_literal_int_constant','lz_parser.py',372),
  ('literal -> DOUBLE_CONST','literal',1,'p_literal_double_constant','lz_parser.py',377),
  ('literal -> STRING_CONST','literal',1,'p_literal_string_constant','lz_parser.py',382),
  ('expression -> VAR','expression',1,'p_expression_var','lz_parser.py',387),
]
