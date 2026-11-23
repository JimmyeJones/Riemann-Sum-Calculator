#Riemann Sum Calculator
#Mattox Jalbert - Fisher AM2
#This site is accessible at: https://riemann-sum-calculator.streamlit.app/
#If prompted, click "Yes" to wake the site.

import streamlit as st

st.title("Riemann Sum Calculator")
st.subheader("Mattox Jalbert - Fisher AM2")
col1, col2, col3 = st.columns(3)

def f(x):
    return (x**2)-4

#Gather user inputs
lb = col1.text_input("Lower Bound")
sub_int = col2.number_input("Number of Subintervals", step=1, min_value=1)
ub = col3.text_input("Upper Bound")
show_points = st.checkbox("Show table with function points")

#Convert inputs
if st.button("Calculate"):
    try:
        lb = float(lb)
        sub_int = int(sub_int)
        ub = float(ub)
        Run = True
    except ValueError:
        st.error("Invalid input")
        Run = False

    #If inputs are valid, calculate sums
    if Run:
        delx = (ub-lb)/sub_int

        #Create list of points on the function with the given number of subintervals
        points = []
        for n in range(sub_int+1):
            xval = lb+(delx*(n))
            yval = f(xval)
            points.append({"xval":xval, "yval":yval})
        st.markdown("---")
        if show_points:
            st.table(points)
        
        #Calculate and display results
        lram_sum = 0
        for point in points[:-1]: #Exclude last point from list
            yval = point["yval"]
            lram_sum += yval*delx
        st.subheader(f"LRAM Sum: {round(lram_sum, 3)}")

        rram_sum = 0
        for point in points[1:]: #Exclude first point from list
            yval = point["yval"]
            rram_sum += yval*delx
        st.subheader(f"RRAM Sum: {round(rram_sum, 3)}")

        mram_sum = 0
        for point in points[:-1]: #Exclude last point from list
            xval1 = point["xval"]
            xval2 = points[points.index(point)+1]["xval"]
            mid_xval = (xval1+xval2)/2 #Calculate x value at midpoint of subinterval
            yval = f(mid_xval)
            mram_sum += yval*delx
        st.subheader(f"MRAM Sum: {round(mram_sum, 3)}")

        trap_sum = 0
        for point in points[:-1]: #Exclude last point from list
            yval1 = point["yval"]
            yval2 = points[points.index(point)+1]["yval"] #Get next y value
            trap_sum += delx*(yval1+yval2)/2 #Add area of the trapezoid to total sum
        st.subheader(f"TRAP Sum: {round(trap_sum, 3)}")