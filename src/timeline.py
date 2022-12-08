"""Classes used to create the timeline."""
import numpy as np
import matplotlib.pyplot as plt


class Age:
    """Object that defines an age.

    In the timeline, adding an age adds a big label at the top, and adds a
    background color to the duration of the age.
    """

    def __init__(
        self,
        start: float,
        end: float,
        color: str,
        y: float = 0.9,
        top_alpha: float = 0.5,
        bottom_alpha=0.1,
        url: str = None,  # type: ignore
    ):
        """
        Parameters
        ----------
        start : float
            Starting year of the age.
        end : float
            Final year of the age.
        color : str
            The color of the age.
        y : float
            The y position of the bottom of the top bar.
        top_alpha : float, default=0.5
            Transparency of the background color at the top bar.
        bottom_alpha : float, default=0.1
            Transparency of background color in the majority of the timeline.
        url : str, default=None
            A url that the title will link to.
        """
        self.start = start
        self.end = end
        self.color = color
        self.y = y
        self.top_alpha = top_alpha
        self.bottom_alpha = bottom_alpha
        self.url = url


class Period:
    """Object that defines a period.

    In the timeline, a period creates a horizontal bar.
    """

    def __init__(
        self,
        start: float,
        end: float,
        y: float,
        color: str,
        alpha: float = 0.4,
        fontsize: float = 10,
        bold: bool = False,
        h: float = 0.025,
        url: str = None,  # type: ignore
    ):
        """
        Parameters
        ----------
        start : float
            Starting year of the age.
        end : float
            Final year of the age.
        y : float
            y position of the bar.
        color : str
            The color of the age.
        alpha : float, default=0.4
            Transparency of the bar.
        fontsize : float, default=10
            Font size of title.
        bold : bool, default=False
            Whether the period title is bolded.
        h : float, default=0.025
            Half the height of the bar. Decreasing makes the bar thinner.
        url : str, default=None
            A url that the title will link to.
        """
        self.start = start
        self.end = end
        self.y = y
        self.color = color
        self.alpha = alpha
        self.fontsize = fontsize
        self.bold = bold
        self.h = h
        self.url = url


class Event:
    """Object that defines an event.

    In the timeline, an event is just text located at position (year, y).
    """

    def __init__(
        self,
        year: float,
        y: float,
        color: str = "k",
        fontsize: float = 8,
        bold: bool = True,
        url: str = None,  # type: ignore
    ):
        """
        Parameters
        ----------
        year : float
            Year of the event.
        y : float
            y position of the event.
        color : str
            The color of the event.
        fontsize : float, default=10
            Font size of event.
        bold : bool, default=True
            Whether or not to bold the title of the event.
        url : str, default=None
            A url that the title will link to.
        """
        self.year = year
        self.y = y
        self.color = color
        self.fontsize = fontsize
        self.bold = bold
        self.url = url


class Country:
    """Object that defines a country.

    In the timeline, countries are labels on the left side of the plot. There
    will also be fences between the countries and the rest of the timeline.
    """

    def __init__(self, y: float, url: str = None):  # type: ignore
        """
        Parameters
        ----------
        y : float
            y position of the country.
        url : str, optional
            A url that the country name will link to.
        """
        self.y = y
        self.url = url


class Timeline:
    """The timeline object!"""

    def __init__(
        self,
    ):
        self.ages = {}
        self.periods = {}
        self.countries = {}
        self.events = {}

    def add_age(
        self,
        name: str,
        start: float,
        end: float,
        color: str,
        y: float = 0.9,
        top_alpha: float = 0.5,
        bottom_alpha: float = 0.1,
        url: str = None,  # type: ignore
    ):
        """Adds an age to the timeline.

        Adding an age adds a big label at the top, and adds a background color
        to the duration of the age.

        Parameters
        ----------
        name : str
            The name of the age.
        start : float
            Starting year of the age.
        end : float
            Final year of the age.
        color : str
            The color of the age.
        y : float
            The y position of the bottom of the top bar.
        top_alpha : float, default=0.5
            Transparency of the background color at the top bar.
        bottom_alpha : float, default=0.1
            Transparency of background color in the majority of the timeline.
        url : str, default=None
            A url that the title will link to.
        """
        self.ages[name] = Age(
            start,
            end,
            color,
            y,
            top_alpha,
            bottom_alpha,
            url,
        )

    def add_period(
        self,
        name: str,
        start: float,
        end: float,
        y: float,
        color: str,
        alpha: float = 0.4,
        fontsize: float = 10,
        bold: bool = False,
        h: float = 0.025,
        url: str = None,  # type: ignore
    ):
        """Adds a period to the timeline.

        Adding a period adds a horizontal bar.

        Parameters
        ----------
        name : str
            The name of the period
        start : float
            Starting year of the age.
        end : float
            Final year of the age.
        y : float
            y position of the bar.
        color : str
            The color of the age.
        alpha : float, default=0.4
            Transparency of the bar.
        fontsize : float, default=10
            Font size of title.
        bold : bool, default=False
            Whether the period title is bolded.
        h : float, default=0.025
            Half the height of the bar. Decreasing makes the bar thinner.
        url : str, default=None
            A url that the title will link to.
        """
        self.periods[name] = Period(
            start,
            end,
            y,
            color,
            alpha,
            fontsize,
            bold,
            h,
            url,
        )

    def add_event(
        self,
        name: str,
        year: float,
        y: float,
        color: str = "k",
        fontsize: float = 8,
        bold: bool = True,
        url: str = None,  # type: ignore
    ):
        """Adds an event to the timeline.

        In the timeline, an event is just text located at position (year, y).

        Parameters
        ----------
        name : str
            The name of the event.
        year : float
            Year of the event.
        y : float
            y position of the event.
        color : str
            The color of the event.
        fontsize : float, default=10
            Font size of event.
        bold : bool, default=True
            Whether or not to bold the title of the event.
        url : str, default=None
            A url that the title will link to.
        """
        self.events[name] = Event(year, y, color, fontsize, bold, url)

    def add_country(
        self,
        name: str,
        y: float,
        url: str = None,  # type: ignore
    ):
        """Adds a country to the timeline.

        Countries are labels on the left side of the plot. There will also be
        fences between the countries and the rest of the timeline.

        Parameters
        ----------
        name : str
            The name of the country.
        y : float
            y position of the country.
        url : str, optional
            A url that the country name will link to.
        """
        self.countries[name] = Country(y, url)

    @property
    def _all_years(
        self,
    ):
        # get all the years from the ages
        ages_years = np.array(
            [[age.start, age.end] for age in self.ages.values()]
        ).flatten()
        # get all the years from the periods
        periods_years = np.array(
            [[age.start, age.end] for age in self.periods.values()]
        ).flatten()
        # get all the years from the events
        events_years = np.array(
            [event.year for event in self.events.values()]
        ).flatten()
        # put them all together in one array
        all_years = np.concatenate((ages_years, periods_years, events_years))

        return all_years

    @property
    def start(
        self,
    ) -> float:
        """Returns the earliest year of the timeline."""
        return np.min(self._all_years)

    @property
    def end(
        self,
    ) -> float:
        """Returns the latest year of the timeline."""
        return np.max(self._all_years)

    def plot(
        self,
        figsize: tuple = (16, 10),
        dpi: int = 100,
        country_offset: float = 10,
        fences: bool = True,
        fence_color: str = "k",
        fence_alpha: float = 0.2,
        hide_yaxis: bool = True,
    ) -> plt.figure:
        """Plot the timeline!

        Parameters
        ----------
        figsize : tuple, default=(16, 10)
            A tuple of floats that sets the size of the figure in inches.
        dpi : int, default=100
            The resolution of the plot. You can adjust this to increase the 
            size of the plot as it shows in the notebook. If you save the 
            figure as a pdf, then the dpi does not matter for the saved file. 
            However, if you save the figure as an image (e.g. a jpg or png), 
            then this also sets the resolution of the saved image. Note you 
            can also supply a dpi keyword when saving the figure as an image, 
            and that value will override this value for the saved image.
        country_offset : float, default=10
            The offset of the country names from the left side of the plot. If
            the country names are running onto the timeline, increase this.
        fences : bool, default=True
            Whether to plot the fences around the countries.
        fence_color : str, default="k"
            Color of the fences.
        fence_alpha : float, default=0.2
            Transparency of the fences.
        hide_yaxis : bool, default
        """
        # create the figure
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

        # plot the ages
        for name, age in self.ages.items():
            # top bar with label
            ax.axvspan(
                age.start,
                age.end,
                age.y,
                1.0,
                color=age.color,
                alpha=age.top_alpha,
                lw=0,
            )
            ax.text(
                np.mean([age.start, age.end]),
                0.95,
                name,
                url=age.url,
                fontsize=12,
                ha="center",
                va="center",
            )

            # color block below
            ax.axvspan(
                age.start,
                age.end,
                0.0,
                age.y,
                color=age.color,
                alpha=age.bottom_alpha,
                lw=0,
            )

        # plot the periods
        for name, period in self.periods.items():
            # create the color bar
            x = np.linspace(period.start, period.end)
            y = period.y
            h = period.h
            ax.fill_between(  # white bar behind
                x,
                y - h,
                y + h,
                color="w",
                lw=0,
            )
            ax.fill_between(  # color bar
                x,
                y - h,
                y + h,
                color=period.color,
                alpha=period.alpha,
                lw=0,
            )

            # label the bar
            weight = "bold" if period.bold else None
            ax.text(
                x.mean(),
                y,
                name,
                url=period.url,
                fontsize=period.fontsize,
                weight=weight,
                ha="center",
                va="center",
            )

        # label the countries
        for name, country in self.countries.items():
            ax.text(
                self.start - country_offset,
                country.y,
                name,
                va="center",
                ha="right",
            )

        # put fences around the countries
        if fences:
            y_countries = np.array(  # get the y positions of every country
                [country.y for country in self.countries.values()]
            )
            # create the list of fences
            if len(y_countries) > 1:
                # fences between each country
                y_fences = (y_countries[1:] + y_countries[:-1]) / 2
                # add fence above top country
                y_fences = np.append(
                    y_fences,
                    2 * np.max(y_countries) - np.max(y_fences),
                )
            else:
                y_fences = 2 * y_countries

            # plot all the fences
            for y in y_fences:
                ax.plot(
                    [self.start, self.end],
                    [y, y],
                    c=fence_color,
                    ls="--",
                    alpha=fence_alpha,
                    zorder=0,
                )

        # plot the events
        for name, event in self.events.items():
            weight = "bold" if event.bold else None
            ax.text(
                event.year,
                event.y,
                name,
                url=event.url,
                c=event.color,
                fontsize=event.fontsize,
                weight=weight,
                va="center",
                ha="center",
            )

        # create the x ticks
        first_tick = ((self.start - 1) // 100 + 1) * 100
        final_tick = (self.end // 100 + 1) * 100
        ax.set(xticks=np.arange(first_tick, final_tick, 100))

        # set the y axis
        ax.set(ylim=(0, 1), xlim=(self.start, self.end))

        # hide the y axis
        if hide_yaxis:
            ax.set(yticks=[])
            for spine in ax.spines.values():
                spine.set_visible(False)

        return fig
