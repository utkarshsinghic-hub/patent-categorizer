from utils.storage import get_project_file
import pandas as pd
import streamlit as st
import os
import shutil

from utils.storage import (
    create_project,
    get_projects,
    delete_project,
    rename_project
)

from utils.template import create_template


st.set_page_config(
    page_title="Patent Categorization Tool",
    layout="wide"
)


st.title("Patent Categorization Tool")
if "page" not in st.session_state:
    st.session_state.page = "home"


# -----------------------------
# HOME PAGE
# -----------------------------

left, right = st.columns(2)


# =============================
# CREATE NEW PROJECT
# =============================

with left:

    st.subheader("Create New Project")

    project_name = st.text_input(
        "Project Name"
    )


    uploaded_file = st.file_uploader(
        "Upload Patent Excel File",
        type=["xlsx"]
    )


    st.download_button(
        label="Download Sample Template",
        data=create_template(),
        file_name="patent_template.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


    if st.button("Create Project"):

        if project_name:

            path = create_project(
                project_name
            )


            if uploaded_file:

                file_path = os.path.join(
                    path,
                    uploaded_file.name
                    ),

                with open(
                    file_path,
                    "wb"
                ) as f:

                    f.write(
                        uploaded_file.getvalue()
                    )

            st.success(
                f"Project '{project_name}' created"
            )

            st.rerun()


        else:

            st.warning(
                "Please enter project name"
            )



# =============================
# EXISTING PROJECTS
# =============================

with right:

    st.subheader(
        "Existing Projects"
    )


    projects = get_projects()


    if not projects:

        st.info(
            "No projects created yet"
        )


    for project in projects:


        with st.container(border=True):

            st.write(
                project
            )


            col1, col2, col3 = st.columns(3)


            with col1:

                if st.button(
                    "Open",
                    key=f"open_{project}"
                ):

                    st.session_state[
                        "current_project"
                    ] = project

                    st.session_state[
                        "page"
                    ] = "workspace"
                    
                    st.rerun()


            with col2:

                if st.button(
                    "Rename",
                    key=f"rename_{project}"
                ):

                    st.session_state[
                        "rename_project"
                    ] = project



            with col3:

                if st.button(
                    "Delete",
                    key=f"delete_{project}"
                ):

                    delete_project(
                        project
                    )

                    st.rerun()



    if "rename_project" in st.session_state:


        old = st.session_state[
            "rename_project"
        ]


        new = st.text_input(
            "New Project Name"
        )


        if st.button(
            "Confirm Rename"
        ):

            if new:

                rename_project(
                    old,
                    new
                )

                del st.session_state[
                    "rename_project"
                ]

                st.rerun()

# ==========================
# PROJECT WORKSPACE
# ==========================

if st.session_state.get("page") == "workspace":

    project = st.session_state[
        "current_project"
    ]


    st.title(
        project
    )


    st.subheader(
        "Patent List"
    )


    file = get_project_file(
        project
    )


    if file:

        df = pd.read_excel(
            file
        )


        st.dataframe(
            df,
            use_container_width=True
        )

        selected_index = st.selectbox(
            "Select Patent",
            df.index
        )

        if st.button("Open Patent"):
            
            st.session_state["selected_patent"] = (
                 df.loc[selected_index]
            )
            
            st.session_state["page"] = "patent"
            
            st.rerun()


    else:

        st.warning(
            "No patent Excel file found"
        )


    if st.button(
        "← Back to Home"
    ):

        st.session_state[
            "page"
        ] = "home"

        st.rerun()

# ==========================
# PATENT DETAIL PAGE
# ==========================

if st.session_state.get("page") == "patent":

    patent = st.session_state[
        "selected_patent"
    ]


    st.title(
        patent["Title"]
    )


    st.subheader(
        "Publication Number"
    )

    st.write(
        patent["Application Number"]
    )


    left,right = st.columns(2)


    with left:

        st.subheader(
            "Abstract"
        )

        st.write(
            patent["Abstract"]
        )


    with right:

        st.subheader(
            "Bibliographic Data"
        )

        st.write(
            "Inventor:"
        )

        st.write(
            "Original Assignee:"
        )

        st.write(
            "Current Assignee:"
        )

        st.write(
            "Priority Date:"
        )

        st.write(
            "Number of Families:"
        )

        st.write(
            "Legal Status:"
        )


    st.subheader(
        "Description"
    )

    st.write(
        patent.get(
            "Description",
            "Not available"
        )
    )


    st.subheader(
        "Claims"
    )

    st.write(
        patent.get(
            "Claims",
            "Not available"
        )
    )


    if st.button(
        "← Back to Patent List"
    ):

        st.session_state["page"] = "workspace"

        st.rerun()
