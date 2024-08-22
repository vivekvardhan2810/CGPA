# CGPA
<p>I had Created a Dataset based upon my Previous academic performances using Credits and GPA Of Each Semester</p>
<p>To calculate the Cumulative Grade Point Average (CGPA), you typically need the GPA for each semester or academic term. If your dataset includes information for multiple terms or semesters, you can calculate the CGPA by averaging the GPAs across all terms.</p>
 <P><b>Steps That I Used for Calculating My CGPA:</b></P>
<P>1. I Added a new column for 'Term Credits' if not already present, representing the total credits for each term.</P>
<p>2. Calculate the 'Term Grade Points' for each term by multiplying 'GPA' with 'Term Credits'.</p>
<p>3. Sum the 'Term Grade Points' and 'Term Credits' columns for all terms.</p>
<p>Calculate the CGPA using the formula: CGPA = Total Term Grade Points / Total Term Credits.</p>

<p>In <b>Conclusion</b>, the provided Python code demonstrates how to calculate the Cumulative Grade Point Average (CGPA) based on a given dataset using the pandas library. The script assumes the presence of columns such as 'GPA' and 'Term Credits' in the dataset, and it follows the standard steps for CGPA calculation, including the multiplication of GPA by term credits and the summation of these values across all terms. The resulting CGPA is then obtained by dividing the total term grade points by the total term credits.</p>

<p> By this we can calculate the CGPA</P>