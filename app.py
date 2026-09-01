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

                with open(
                    os.path.join(
                        path,
                        uploaded_file.name
                    ),
                    "wb"
                ) as f:

                    f.write(
                        uploaded_file.getbuffer()
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

                    st.success(
                        f"Opened {project}"
                    )


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
