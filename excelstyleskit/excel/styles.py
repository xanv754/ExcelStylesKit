from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.styles.colors import Color
from excelstyleskit.excel.excel import ExcelManager


class ExcelStyle:
    _excel: ExcelManager

    def __init__(self, excel: ExcelManager) -> None:
        self._excel = excel

    def set_background(self, hex_color: str) -> bool:
        """Sets the fill color for all cells in the Excel table.

        Parameters:
        ----------
        hex_color : str
            Hexadecimal color to apply.

        Returns:
        --------
        bool : Returns `True` if styles were applied successfully, `False` otherwise.
        """
        try:
            color = Color(rgb=hex_color, type="rgb")
            fill = PatternFill(patternType="solid",
                               start_color=color, end_color=color)
            self._excel.apply_style_body(property="fill", value=fill)
        except Exception as error:
            print("ExcelStyle Error", error)
            return False
        else:
            return True

    def set_font(
        self,
        type: str = "Time New Roman",
        size: float = 10.0,
        bold: bool = False,
        italic: bool = False,
        hex_color: str = "FFFF0000",
    ) -> bool:
        """Sets the font for all cells in the Excel table.

        Parameters:
        ----------
        type : str, optional
            Font type name.
        size : float, optional
            Size font.
        bold : bool, optional
            Bold type.
        italic : bool, optional
            Italic type.
        hex_color : str, optional
            Hexadecimal color to apply.
        Returns:
        --------
        bool : Returns `True` if styles were applied successfully, `False` otherwise.
        """
        try:
            color = Color(rgb=hex_color, type="rgb")
            font = Font(name=type, size=size, bold=bold,
                        italic=italic, color=color)
            self._excel.apply_style_body(property="font", value=font)
        except Exception as error:
            print("ExcelStyle Error", error)
            return False
        else:
            return True

    def set_alignment(
        self,
        horizontal: str = "left",
        vertical: str = "center",
        wrap_text: bool = False,
    ) -> None:
        """Sets the alignment text for all cells in the Excel table.

        Parameters:
        ----------
        horizontal : str, optional
            Horizontal text centering.
        vertical : str, optional
            Vertical text centering.
        wrap_text : bool, optional
            Wrap text.
        Returns:
        --------
        bool : Returns `True` if styles were applied successfully, `False` otherwise.
        """
        try:
            alignment = Alignment(
                horizontal=horizontal, vertical=vertical, wrap_text=wrap_text
            )
            self._excel.apply_style_body(property="alignment", value=alignment)
        except Exception as error:
            print("ExcelStyle Error", error)
            return False
        else:
            return True

    def set_border(
        self,
        left: bool = True,
        left_style: str = "thin",
        right: bool = True,
        right_style: str = "thin",
        top: bool = True,
        top_style: str = "thin",
        bottom: bool = True,
        bottom_style: str = "thin",
        hex_color: str = "000000",
    ) -> None:
        """Sets the border for all cells in the Excel table.

        Parameters:
        ----------
        left : bool, optional
            If True, enables the left border.
        left_style : str, optional
            The style or type of the left border.
        right : bool, optional
            If True, enables the right border.
        right_style : str, optional
            The style or type of the right border.
        top : bool, optional
            If True, enables the top border.
        top_style : str, optional
            The style or type of the top border.
        bottom : bool, optional
            If True, enables the bottom border.
        bottom_style : str, optional
            The style or type of the bottom border.
        hex_color : str, optional
            Hexadecimal color to apply.
        Returns:
        --------
        bool : Returns `True` if styles were applied successfully, `False` otherwise.
        """
        try:
            color = Color(rgb=hex_color, type="rgb")
            border = Border(
                left=Side(style=left_style, color=color) if left else None,
                right=Side(style=right_style, color=color) if right else None,
                top=Side(style=top_style, color=color) if top else None,
                bottom=Side(style=bottom_style,
                            color=color) if bottom else None,
            )
            self._excel.apply_style_body(property="border", value=border)
        except Exception as error:
            print("ExcelStyle Error", error)
            return False
        else:
            return True

# ----------------- HEADERS ---------------------------------

    def set_header_background(self, hex_color: str) -> bool:
        """Sets the fill color for all cells in the header Excel table.

        Parameters:
        ----------
        hex_color : str
            Hexadecimal color to apply.

        Returns:
        --------
        bool : Returns `True` if styles were applied successfully, `False` otherwise.
        """
        try:
            color = Color(rgb=hex_color, type="rgb")
            fill = PatternFill(patternType="solid",
                               start_color=color, end_color=color)
            self._excel.apply_style_header(property="fill", value=fill)
        except Exception as error:
            print("ExcelStyle Error", error)
            return False
        else:
            return True

    def set_header_font(
        self,
        type: str = "Time New Roman",
        size: float = 10.0,
        bold: bool = False,
        italic: bool = False,
        hex_color: str = "FFFF0000",
    ) -> bool:
        """Sets the font for all cells in the header Excel table.

        Parameters:
        ----------
        type : str, optional
            Font type name.
        size : float, optional
            Size font.
        bold : bool, optional
            Bold type.
        italic : bool, optional
            Italic type.
        hex_color : str, optional
            Hexadecimal color to apply.
        Returns:
        --------
        bool : Returns `True` if styles were applied successfully, `False` otherwise.
        """
        try:
            color = Color(rgb=hex_color, type="rgb")
            font = Font(name=type, size=size, bold=bold,
                        italic=italic, color=color)
            self._excel.apply_style_header(property="font", value=font)
        except Exception as error:
            print("ExcelStyle Error", error)
            return False
        else:
            return True

    def set_header_alignment(
        self,
        horizontal: str = "left",
        vertical: str = "center",
        wrap_text: bool = False,
    ) -> None:
        """Sets the alignment text for all cells in the header Excel table.

        Parameters:
        ----------
        horizontal : str, optional
            Horizontal text centering.
        vertical : str, optional
            Vertical text centering.
        wrap_text : bool, optional
            Wrap text.
        Returns:
        --------
        bool : Returns `True` if styles were applied successfully, `False` otherwise.
        """
        try:
            alignment = Alignment(
                horizontal=horizontal, vertical=vertical, wrap_text=wrap_text
            )
            self._excel.apply_style_header(
                property="alignment", value=alignment)
        except Exception as error:
            print("ExcelStyle Error", error)
            return False
        else:
            return True

    def set_header_border(
        self,
        left: bool = True,
        left_style: str = "thin",
        right: bool = True,
        right_style: str = "thin",
        top: bool = True,
        top_style: str = "thin",
        bottom: bool = True,
        bottom_style: str = "thin",
        hex_color: str = "000000",
    ) -> None:
        """Sets the border for all cells in the header Excel table.

        Parameters:
        ----------
        left : bool, optional
            If True, enables the left border.
        left_style : str, optional
            The style or type of the left border.
        right : bool, optional
            If True, enables the right border.
        right_style : str, optional
            The style or type of the right border.
        top : bool, optional
            If True, enables the top border.
        top_style : str, optional
            The style or type of the top border.
        bottom : bool, optional
            If True, enables the bottom border.
        bottom_style : str, optional
            The style or type of the bottom border.
        hex_color : str, optional
            Hexadecimal color to apply.
        Returns:
        --------
        bool : Returns `True` if styles were applied successfully, `False` otherwise.
        """
        try:
            color = Color(rgb=hex_color, type="rgb")
            border = Border(
                left=Side(style=left_style, color=color) if left else None,
                right=Side(style=right_style, color=color) if right else None,
                top=Side(style=top_style, color=color) if top else None,
                bottom=Side(style=bottom_style,
                            color=color) if bottom else None,
            )
            self._excel.apply_style_header(property="border", value=border)
        except Exception as error:
            print("ExcelStyle Error", error)
            return False
        else:
            return True
