from Checkers.constants import ROWS,COLS,WHITE,BLACK
import pygame
from copy import deepcopy
import itertools 


def simulate_move(board,piece,move):
    new_board = deepcopy(board)
    list_new_boards = []
    new_piece = new_board.board[piece.row][piece.col]
    if isinstance(move,dict):
        for landing_row,landing_col in move.keys():
            board_copy = deepcopy(new_board)
            piece_copy = board_copy.board[new_piece.row][new_piece.col]
            board_copy, _,became_king = piece_copy.capture_piece(move, board_copy, landing_row, landing_col)
            
            if became_king:
                list_new_boards.append(board_copy)
                continue
            # Chain capture logic
            next_captures = piece_copy.get_capture_moves(board_copy.board)
            if next_captures:
                boards_after_chain = simulate_move(board_copy, piece_copy, next_captures)
                list_new_boards.extend(boards_after_chain)
            else:
                list_new_boards.append(board_copy)
    else:
        for row,col in move:
            tmp = new_piece.make_move(move,new_board,row,col)
            list_new_boards.append(tmp)
    return list_new_boards


def get_all_possible_moves(board,color):
        capture_moves = []
        moves = []

        for row in range(ROWS):
            for col in range(COLS):
                piece = board.board[row][col]
                if piece and piece.color == color:
                    capture_move = piece.get_capture_moves(board.board)
                    if capture_move:
                        capture_moves.append([capture_move,piece])
                    move = piece.get_moves(board.board)
                    if move:
                        moves.append([move,piece])
        

        possible_boards = []
        if capture_moves:
            for move,piece in capture_moves:
                possible_boards += simulate_move(board,piece,move)
        else:
            for move,piece in moves:
                possible_boards += simulate_move(board,piece,move)
        return possible_boards

def minimax(board,depth,maximizing_player,alpha = float("-inf"),beta = float("inf")):
    if depth == 0 or board.game_over():
        return board.evaluate_board(),board

    if maximizing_player:
        max_eval = float("-inf")
        all_pos = get_all_possible_moves(board,WHITE)
        correct_move = None
        for board in all_pos:
            val = minimax(board,depth-1,not maximizing_player,alpha,beta)[0]
            max_eval = max(max_eval,val)
            alpha = max(alpha,val)
            
            if val == max_eval:
                correct_move = board
            
            if beta <= alpha:
                break

        return max_eval,correct_move
    else:
        min_eval = float("inf")
        all_pos = get_all_possible_moves(board,BLACK)
        correct_move = None
        for board in all_pos:
            val = minimax(board,depth-1,not maximizing_player,alpha,beta)[0]
            min_eval = min(min_eval,val)
            beta = min(beta,val)
            if val == min_eval:
                correct_move = board

            if beta <= alpha:
                break
        return min_eval,correct_move